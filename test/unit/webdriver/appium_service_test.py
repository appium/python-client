#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from unittest.mock import Mock, call

import pytest

from appium.webdriver import appium_service
from appium.webdriver.appium_service import AppiumService, AppiumServiceError


class TestAppiumService:
    def test_get_instance(self):
        assert AppiumService()

    def test_get_node_found(self, monkeypatch):
        monkeypatch.setattr(appium_service.shutil, 'which', lambda cmd: f'/usr/bin/{cmd}')
        assert appium_service.get_node() == '/usr/bin/node'

    def test_get_node_not_found(self, monkeypatch):
        monkeypatch.setattr(appium_service.shutil, 'which', lambda cmd: None)
        with pytest.raises(AppiumServiceError, match='NodeJS main executable cannot be found'):
            appium_service.get_node()

    def test_get_npm_found(self, monkeypatch):
        monkeypatch.setattr(appium_service.shutil, 'which', lambda cmd: f'/usr/bin/{cmd}')
        assert appium_service.get_npm() == '/usr/bin/npm'

    def test_get_npm_not_found(self, monkeypatch):
        monkeypatch.setattr(appium_service.shutil, 'which', lambda cmd: None)
        with pytest.raises(AppiumServiceError, match='Node Package Manager executable cannot be found'):
            appium_service.get_npm()

    @pytest.mark.parametrize(
        ('status', 'expected_result', 'expected_elapsed', 'expected_requests'),
        [(200, True, 0.0, 1), (503, False, 5.0, 10)],
    )
    def test_is_listening_uses_five_second_polling_timeout(
        self, monkeypatch, status, expected_result, expected_elapsed, expected_requests
    ):
        process = Mock()
        process.poll.return_value = None
        monkeypatch.setattr(appium_service.sp, 'Popen', Mock(return_value=process))
        service = AppiumService()
        service.start(node='node', npm='npm', main_script='appium.js', timeout_ms=0)

        clock = Mock()
        clock.perf_counter.return_value = 0.0

        def advance_time(seconds):
            clock.perf_counter.return_value += seconds

        clock.sleep.side_effect = advance_time
        monkeypatch.setattr(appium_service, 'time', clock)

        connection = Mock()
        connection.request.return_value.status = status
        monkeypatch.setattr(appium_service.urllib3, 'PoolManager', Mock(return_value=connection))

        assert service.is_listening is expected_result
        assert clock.perf_counter.return_value == expected_elapsed
        assert connection.request.call_args_list == [call('HEAD', 'http://127.0.0.1:4723/status')] * expected_requests

    @pytest.mark.parametrize(
        ('poll_result', 'is_service_listening', 'expected_message'),
        [
            (None, Mock(return_value=False), 'Appium server has started but is not listening'),
            (1, Mock(side_effect=appium_service.AppiumStartupError), 'Appium server process is unable to start'),
        ],
    )
    def test_start_failure_terminates_process_before_reading_stderr(
        self, monkeypatch, poll_result, is_service_listening, expected_message
    ):
        process = Mock()
        process.poll.return_value = poll_result
        process.communicate.return_value = (b'', b'startup error details')
        monkeypatch.setattr(appium_service.sp, 'Popen', Mock(return_value=process))
        monkeypatch.setattr(appium_service, 'is_service_listening', is_service_listening)

        with pytest.raises(AppiumServiceError, match=expected_message) as excinfo:
            AppiumService().start(
                node='node', npm='npm', main_script='appium.js', timeout_ms=1000, stderr=appium_service.sp.PIPE
            )

        assert "Original error: b'startup error details'" in str(excinfo.value)
        # Reading stderr of a process that is still running blocks until the process exits
        process.stderr.read.assert_not_called()
        method_names = [name for name, _, _ in process.method_calls]
        assert method_names.index('terminate') < method_names.index('communicate')

    @pytest.mark.parametrize(
        ('communicate_results', 'expected_error'),
        [
            (
                [appium_service.sp.TimeoutExpired('appium', 5.5), (b'', b'startup error details')],
                "b'startup error details'",
            ),
            (
                [
                    appium_service.sp.TimeoutExpired('appium', 5.5),
                    appium_service.sp.TimeoutExpired('appium', 5.5, stderr=b'partial error details'),
                ],
                "b'partial error details'",
            ),
        ],
    )
    def test_start_failure_keeps_stderr_if_process_ignores_terminate(self, monkeypatch, communicate_results, expected_error):
        process = Mock()
        process.poll.return_value = None
        process.communicate.side_effect = communicate_results

        def kill():
            process.poll.return_value = -9

        process.kill.side_effect = kill
        monkeypatch.setattr(appium_service.sp, 'Popen', Mock(return_value=process))
        monkeypatch.setattr(appium_service, 'is_service_listening', Mock(return_value=False))

        with pytest.raises(AppiumServiceError, match='Appium server has started but is not listening') as excinfo:
            AppiumService().start(
                node='node', npm='npm', main_script='appium.js', timeout_ms=1000, stderr=appium_service.sp.PIPE
            )

        assert f'Original error: {expected_error}' in str(excinfo.value)
        process.kill.assert_called_once()
