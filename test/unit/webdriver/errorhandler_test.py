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

import httpretty
import pytest
from selenium.common.exceptions import (
    InvalidArgumentException,
    InvalidSessionIdException,
    NoSuchElementException,
    StaleElementReferenceException,
    UnexpectedAlertPresentException,
    UnknownMethodException,
    WebDriverException,
)
from selenium.webdriver.common.by import By

from appium.common.exceptions import InvalidSwitchToTargetException, NoSuchContextException
from appium.webdriver.errorhandler import MobileErrorHandler, format_stacktrace
from test.unit.helper.test_helper import android_w3c_driver, appium_command


class TestMobileErrorHandler:
    def test_w3c_error_response(self) -> None:
        handler = MobileErrorHandler()
        response = {
            'status': 404,
            'value': (
                '{"value": {"error": "no such element", "message": "Unable to locate element", "stacktrace": "line1\\nline2"}}'
            ),
        }
        with pytest.raises(NoSuchElementException) as exc_info:
            handler.check_response(response)

        assert exc_info.value.msg is not None
        assert exc_info.value.msg.startswith('Unable to locate element')
        assert exc_info.value.stacktrace == ['line1', 'line2']

    def test_w3c_error_response_without_http_status(self) -> None:
        handler = MobileErrorHandler()
        response = {
            'value': '{"value": {"error": "stale element reference", "message": "Element is stale"}}',
        }
        with pytest.raises(StaleElementReferenceException) as exc_info:
            handler.check_response(response)

        assert exc_info.value.msg is not None
        assert exc_info.value.msg.startswith('Element is stale')

    def test_unexpected_alert_extracts_w3c_data_text(self) -> None:
        handler = MobileErrorHandler()
        response = {
            'status': 500,
            'value': (
                '{"value": {"error": "unexpected alert open", '
                '"message": "Alert is blocking command", '
                '"stacktrace": "", "data": {"text": "Allow notifications?"}}}'
            ),
        }
        with pytest.raises(UnexpectedAlertPresentException) as exc_info:
            handler.check_response(response)

        assert exc_info.value.msg is not None
        assert exc_info.value.msg.startswith('Alert is blocking command')
        assert exc_info.value.alert_text == 'Allow notifications?'
        assert 'Alert Text: Allow notifications?' in str(exc_info.value)

    def test_unexpected_alert_extracts_legacy_alert_or_string_data(self) -> None:
        handler = MobileErrorHandler()
        alert_response = {
            'status': 500,
            'value': '{"value": {"error": "unexpected alert open", "message": "Blocked", "alert": {"text": "Confirm?"}}}',
        }
        with pytest.raises(UnexpectedAlertPresentException) as alert_exc:
            handler.check_response(alert_response)
        assert alert_exc.value.alert_text == 'Confirm?'

        str_response = {
            'status': 500,
            'value': '{"value": {"error": "unexpected alert open", "message": "Blocked", "data": "Legacy alert"}}',
        }
        with pytest.raises(UnexpectedAlertPresentException) as str_exc:
            handler.check_response(str_response)
        assert str_exc.value.alert_text == 'Legacy alert'

    def test_context_specific_exceptions(self) -> None:
        handler = MobileErrorHandler()

        with pytest.raises(NoSuchContextException) as missing_ctx:
            handler.check_response(
                {'status': 400, 'value': '{"value": {"error": "unknown error", "message": "No such context found."}}'}
            )
        assert missing_ctx.value.msg == 'No such context found.'

        with pytest.raises(InvalidSwitchToTargetException) as invalid_ctx:
            handler.check_response(
                {
                    'status': 400,
                    'value': (
                        '{"value": {"error": "unknown error", '
                        '"message": "That command could not be executed in the current context."}}'
                    ),
                }
            )
        assert invalid_ctx.value.msg == 'That command could not be executed in the current context.'

    @pytest.mark.parametrize(
        ('response', 'expected_exc', 'expected_msg'),
        [
            ({'status': 401, 'value': 'Authorization Required'}, WebDriverException, 'Authorization Required'),
            ({'status': 502, 'value': '<html>502 Bad Gateway</html>'}, WebDriverException, '<html>502 Bad Gateway</html>'),
            ({'status': 405, 'value': 'Method Not Allowed'}, UnknownMethodException, 'Method Not Allowed'),
            ({'status': 500, 'value': ''}, WebDriverException, 'HTTP error status: 500'),
            ({'status': 500, 'value': '["unexpected"]'}, WebDriverException, '["unexpected"]'),
            (
                {'status': 404, 'value': '{"error": "invalid session id", "message": "Session expired"}'},
                InvalidSessionIdException,
                'Session expired',
            ),
            (
                {'status': 400, 'value': {'error': 'invalid argument', 'message': 'Invalid timeout value'}},
                InvalidArgumentException,
                'Invalid timeout value',
            ),
            (
                {'status': 500, 'value': '{"value": "Plain error string"}'},
                WebDriverException,
                'Plain error string',
            ),
            (
                {'status': 500, 'value': '{}'},
                WebDriverException,
                '{}',
            ),
        ],
    )
    def test_non_w3c_http_error_responses_raise(
        self, response: dict, expected_exc: type[WebDriverException], expected_msg: str
    ) -> None:
        handler = MobileErrorHandler()
        with pytest.raises(expected_exc) as exc_info:
            handler.check_response(response)
        assert exc_info.value.msg is not None
        assert exc_info.value.msg.startswith(expected_msg)

    def test_jsonwp_error_with_camelcase_stacktrace(self) -> None:
        handler = MobileErrorHandler()
        response = {
            'status': 500,
            'value': (
                '{"status": 7, "value": {"message": "Element missing", "screen": "base64img", '
                '"stackTrace": [{"className": "AppDriver", "methodName": "find", '
                '"fileName": "AppDriver.java", "lineNumber": 42}]}}'
            ),
        }
        with pytest.raises(NoSuchElementException) as exc_info:
            handler.check_response(response)

        assert exc_info.value.msg is not None
        assert exc_info.value.msg.startswith('Element missing')
        assert exc_info.value.screen == 'base64img'
        assert exc_info.value.stacktrace == ['    at AppDriver.find (AppDriver.java:42)']

    def test_non_error_responses_do_not_raise(self) -> None:
        handler = MobileErrorHandler()
        handler.check_response({'status': 0, 'value': 'iVBORw0KGgoAAAANSUhEUg=='})
        handler.check_response({'value': None})
        handler.check_response({'value': 'plain result'})
        handler.check_response({'value': {'value': {'arbitrary': 'data'}}})
        handler.check_response({'value': {'error': 'user script key', 'message': 'not a webdriver error'}})

    def test_format_stacktrace(self) -> None:
        assert format_stacktrace(None) == []
        assert format_stacktrace('line1\nline2') == ['line1', 'line2']
        assert format_stacktrace(
            [
                {'className': 'Foo', 'methodName': 'bar', 'fileName': 'Foo.java', 'lineNumber': 12},
                'invalid-frame',  # type: ignore[list-item]
                {'methodName': 'baz'},
            ]
        ) == ['    at Foo.bar (Foo.java:12)', '    at baz (<anonymous>)']

    @httpretty.activate
    def test_driver_raises_on_http_proxy_and_auth_errors(self) -> None:
        driver = android_w3c_driver()

        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            status=401,
            body='Unauthorized',
        )
        with pytest.raises(WebDriverException) as auth_exc:
            driver.find_element(By.ID, 'btn')
        assert auth_exc.value.msg == 'Authorization Required'

        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/settings'),
            status=502,
            body='<html>502 Bad Gateway</html>',
        )
        with pytest.raises(WebDriverException) as gateway_exc:
            driver.get_settings()
        assert gateway_exc.value.msg == '<html>502 Bad Gateway</html>'

    @httpretty.activate
    def test_driver_raises_unexpected_alert_with_text(self) -> None:
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/element'),
            status=500,
            body=(
                '{"value": {"error": "unexpected alert open", '
                '"message": "unexpected alert open", '
                '"stacktrace": "", "data": {"text": "Allow location?"}}}'
            ),
        )
        with pytest.raises(UnexpectedAlertPresentException) as exc_info:
            driver.find_element(By.ID, 'btn')
        assert exc_info.value.alert_text == 'Allow location?'

    @httpretty.activate
    def test_driver_allows_http_200_user_dict_with_error_key(self) -> None:
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/execute/sync'),
            status=200,
            content_type='application/json',
            body='{"value": {"error": "timeout", "message": "app payload"}}',
        )
        result = driver.execute_script('return arguments[0]', {'ok': True})
        assert result == {'error': 'timeout', 'message': 'app payload'}
