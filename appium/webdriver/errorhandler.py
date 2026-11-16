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

import json
from http import HTTPStatus
from typing import Any

import selenium.common.exceptions as sel_exceptions
from selenium.webdriver.remote import errorhandler

import appium.common.exceptions as appium_exceptions


class MobileErrorHandler(errorhandler.ErrorHandler):
    def check_response(self, response: dict[str, Any]) -> None:
        """Handle W3C and HTTP error responses, retaining Appium-specific exception mappings."""
        status = response.get('status')
        if status == errorhandler.ErrorCode.SUCCESS and not isinstance(status, bool):
            return

        http_error_status = (
            status if isinstance(status, int) and not isinstance(status, bool) and status >= HTTPStatus.BAD_REQUEST else None
        )
        payload = response.get('value', '')
        payload_dict = _parse_payload_dict(payload)

        if payload_dict is None:
            if http_error_status is not None:
                self._raise_http_error(http_error_status, payload if isinstance(payload, str) else '')
            return

        value = payload_dict.get('value')
        is_jsonwp_dict = 'status' in payload_dict and not isinstance(payload_dict.get('error'), str)
        if isinstance(value, dict):
            error = value.get('error')
            if isinstance(error, str) and error:
                self._delegate_w3c_error(error, value)
                return
            if http_error_status is not None and not is_jsonwp_dict:
                self._raise_http_error(http_error_status, json.dumps(payload_dict))
            return

        if http_error_status is None or is_jsonwp_dict:
            return

        flat_error = payload_dict.get('error')
        if isinstance(flat_error, str) and flat_error:
            self._delegate_w3c_error(flat_error, payload_dict)
            return

        raw_msg = value if isinstance(value, str) and value else json.dumps(payload_dict)
        self._raise_http_error(http_error_status, raw_msg)

    def _delegate_w3c_error(self, error: str, value: dict[str, Any]) -> None:
        normalized = {**value, 'data': {'text': value['data']}} if isinstance(value.get('data'), str) else value
        try:
            super().check_response({'status': error, 'value': normalized})
        except sel_exceptions.WebDriverException as exc:
            if type(exc) is not sel_exceptions.WebDriverException:
                raise
            exception_class: type[sel_exceptions.WebDriverException]
            if error in ('unknown command', 'unknown method', 'unsupported operation'):
                exception_class = sel_exceptions.UnknownMethodException
            elif exc.msg == 'No such context found.':
                exception_class = appium_exceptions.NoSuchContextException
            elif exc.msg == 'That command could not be executed in the current context.':
                exception_class = appium_exceptions.InvalidSwitchToTargetException
            else:
                raise
            raise exception_class(msg=exc.msg, screen=exc.screen, stacktrace=exc.stacktrace) from exc

    def _raise_http_error(self, status: int, text: str) -> None:
        msg = text or f'HTTP error status: {status}'
        if status == HTTPStatus.METHOD_NOT_ALLOWED:
            raise sel_exceptions.UnknownMethodException(msg=msg)
        raise sel_exceptions.WebDriverException(msg=msg)


def _parse_payload_dict(payload: Any) -> dict[str, Any] | None:
    if isinstance(payload, dict):
        return payload
    if isinstance(payload, str):
        try:
            loaded = json.loads(payload)
        except (json.JSONDecodeError, TypeError):
            return None
        return loaded if isinstance(loaded, dict) else None
    return None
