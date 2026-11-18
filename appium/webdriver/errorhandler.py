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
        payload = response.get('value', '')
        payload_dict = _parse_payload_dict(payload)
        w3c_error = _extract_w3c_error(payload_dict)
        if w3c_error is None:
            _raise_if_http_error(response, payload, payload_dict)
            return

        error, value = w3c_error
        # Pass the W3C error string as Selenium's internal status, never a
        # JSONWP numeric status. Selenium handles data.text and stacktrace.
        try:
            super().check_response({'status': error, 'value': value})
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


def _parse_payload_dict(payload: Any) -> dict[str, Any] | None:
    if isinstance(payload, dict):
        return payload
    if isinstance(payload, str):
        try:
            loaded = json.loads(payload)
        except ValueError:
            return None
        return loaded if isinstance(loaded, dict) else None
    return None


def _extract_w3c_error(payload_dict: dict[str, Any] | None) -> tuple[str, dict[str, Any]] | None:
    if payload_dict is None:
        return None
    value = payload_dict.get('value')
    if not isinstance(value, dict):
        return None
    error = value.get('error')
    if not isinstance(error, str) or not error:
        return None
    return error, value


def _raise_if_http_error(response: dict[str, Any], payload: Any, payload_dict: dict[str, Any] | None) -> None:
    status = response.get('status')
    if not isinstance(status, int) or isinstance(status, bool) or status < HTTPStatus.BAD_REQUEST:
        return
    if payload_dict is None:
        msg = payload if isinstance(payload, str) and payload else f'HTTP error status: {status}'
        raise sel_exceptions.WebDriverException(msg=msg)
    if 'status' in payload_dict:
        return
    value = payload_dict.get('value')
    msg = value if isinstance(value, str) and value else json.dumps(payload_dict)
    raise sel_exceptions.WebDriverException(msg=msg)
