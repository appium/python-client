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

from unittest.mock import Mock

import pytest

from appium.webdriver import appium_service
from appium.webdriver.appium_service import AppiumService


class TestAppiumService:
    def test_get_instance(self):
        assert AppiumService()

    @pytest.mark.parametrize(
        ('status', 'expected_result', 'expected_elapsed'),
        [(200, True, 0.0), (503, False, 0.5)],
    )
    def test_is_listening_uses_short_polling_timeout(self, monkeypatch, status, expected_result, expected_elapsed):
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
        connection.request.assert_called_once_with('HEAD', 'http://127.0.0.1:4723/status')
