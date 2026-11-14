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
from collections.abc import Sequence
from typing import Any

import selenium.common.exceptions as sel_exceptions
from selenium.webdriver.remote import errorhandler

import appium.common.exceptions as appium_exceptions

ERROR_TO_EXC_MAPPING: dict[str, type[sel_exceptions.WebDriverException]] = {
    'element click intercepted': sel_exceptions.ElementClickInterceptedException,
    'element not interactable': sel_exceptions.ElementNotInteractableException,
    'insecure certificate': sel_exceptions.InsecureCertificateException,
    'invalid argument': sel_exceptions.InvalidArgumentException,
    'invalid cookie domain': sel_exceptions.InvalidCookieDomainException,
    'invalid element state': sel_exceptions.InvalidElementStateException,
    'invalid selector': sel_exceptions.InvalidSelectorException,
    'invalid session id': sel_exceptions.InvalidSessionIdException,
    'javascript error': sel_exceptions.JavascriptException,
    'move target out of bounds': sel_exceptions.MoveTargetOutOfBoundsException,
    'no such alert': sel_exceptions.NoAlertPresentException,
    'no such cookie': sel_exceptions.NoSuchCookieException,
    'no such element': sel_exceptions.NoSuchElementException,
    'no such frame': sel_exceptions.NoSuchFrameException,
    'no such window': sel_exceptions.NoSuchWindowException,
    'no such shadow root': sel_exceptions.NoSuchShadowRootException,
    'script timeout': sel_exceptions.TimeoutException,
    'session not created': sel_exceptions.SessionNotCreatedException,
    'stale element reference': sel_exceptions.StaleElementReferenceException,
    'detached shadow root': sel_exceptions.NoSuchShadowRootException,
    'timeout': sel_exceptions.TimeoutException,
    'unable to set cookie': sel_exceptions.UnableToSetCookieException,
    'unable to capture screen': sel_exceptions.ScreenshotException,
    'unexpected alert open': sel_exceptions.UnexpectedAlertPresentException,
    'unknown command': sel_exceptions.UnknownMethodException,
    'unknown error': sel_exceptions.WebDriverException,
    'unknown method': sel_exceptions.UnknownMethodException,
    'unsupported operation': sel_exceptions.UnknownMethodException,
    'element not visible': sel_exceptions.ElementNotVisibleException,
    'element not selectable': sel_exceptions.ElementNotSelectableException,
    'invalid coordinates': sel_exceptions.InvalidCoordinatesException,
}


def format_stacktrace(original: None | str | Sequence) -> list[str]:
    if not original:
        return []
    if isinstance(original, str):
        return original.split('\n')

    result: list[str] = []
    try:
        for frame in original:
            if not isinstance(frame, dict):
                continue

            line = frame.get('lineNumber', '')
            file = frame.get('fileName', '<anonymous>')
            if line:
                file = f'{file}:{line}'
            meth = frame.get('methodName', '<anonymous>')
            if 'className' in frame:
                meth = f'{frame["className"]}.{meth}'
            result.append(f'    at {meth} ({file})')
    except TypeError:
        pass
    return result


JSONWP_ERROR_CODE_MAP: dict[int, str] = {
    7: 'no such element',
    8: 'no such frame',
    9: 'unknown command',
    10: 'stale element reference',
    11: 'element not visible',
    12: 'invalid element state',
    13: 'unknown error',
    15: 'element not selectable',
    17: 'javascript error',
    19: 'invalid selector',
    21: 'timeout',
    23: 'no such window',
    24: 'invalid cookie domain',
    25: 'unable to set cookie',
    26: 'unexpected alert open',
    27: 'no such alert',
    28: 'script timeout',
    29: 'invalid coordinates',
    32: 'invalid selector',
    33: 'session not created',
    34: 'move target out of bounds',
    51: 'invalid selector',
    52: 'invalid selector',
    60: 'element not interactable',
    61: 'invalid argument',
    62: 'no such cookie',
    63: 'unable to capture screen',
    64: 'element click intercepted',
    65: 'detached shadow root',
    405: 'unsupported operation',
}


def _parse_payload_dict(payload: Any) -> dict[str, Any] | None:
    """Parse an error payload into a dict if it contains a JSON object."""
    if isinstance(payload, dict):
        return payload
    if isinstance(payload, str):
        try:
            loaded = json.loads(payload)
        except (json.JSONDecodeError, TypeError):
            return None
        return loaded if isinstance(loaded, dict) else None
    return None


def _extract_alert_text(value: dict[str, Any]) -> str | None:
    """Extract the alert prompt string from W3C `data.text` or legacy fields."""
    data = value.get('data')
    if isinstance(data, dict):
        text = data.get('text')
        return text if isinstance(text, str) else None
    if isinstance(data, str):
        return data
    alert = value.get('alert')
    if isinstance(alert, dict):
        text = alert.get('text')
        return text if isinstance(text, str) else None
    return None


def _resolve_exception_class(error: Any, message: str | None) -> type[sel_exceptions.WebDriverException]:
    """Resolve a W3C error string, JSONWP numeric status, or Appium message to an exception class."""
    error_key = error
    if isinstance(error, int) and not isinstance(error, bool):
        error_key = JSONWP_ERROR_CODE_MAP.get(error)
    exception_class: type[sel_exceptions.WebDriverException] = (
        ERROR_TO_EXC_MAPPING.get(error_key, sel_exceptions.WebDriverException)
        if isinstance(error_key, str)
        else sel_exceptions.WebDriverException
    )
    if exception_class is sel_exceptions.WebDriverException and message:
        if message == 'No such context found.':
            return appium_exceptions.NoSuchContextException
        if message == 'That command could not be executed in the current context.':
            return appium_exceptions.InvalidSwitchToTargetException
    return exception_class


class MobileErrorHandler(errorhandler.ErrorHandler):
    def check_response(self, response: dict[str, Any]) -> None:
        """
        https://www.w3.org/TR/webdriver/#errors
        """
        status = response.get('status')
        if status == errorhandler.ErrorCode.SUCCESS and not isinstance(status, bool):
            return

        has_error_status = bool(status)
        payload = response.get('value', '')
        payload_dict = _parse_payload_dict(payload)
        fallback_msg = (
            payload if isinstance(payload, str) and payload else response.get('message') or f'HTTP error status: {status}'
        )

        error_dict: dict[str, Any] = {}
        error_identifier: Any = status
        if payload_dict is None:
            if not has_error_status:
                return
            message = fallback_msg
        else:
            nested_value = payload_dict.get('value')
            if isinstance(nested_value, dict):
                error_dict = nested_value
                error = error_dict.get('error')
                if not error and not has_error_status:
                    return
                error_identifier = error or payload_dict.get('status') or status
                message = error_dict.get('message') or payload_dict.get('message') or error or fallback_msg
            else:
                # Flat response dicts without an error status can be valid HTTP 200 command results.
                if not has_error_status:
                    return
                error_dict = payload_dict
                error_identifier = payload_dict.get('error') or payload_dict.get('status') or status
                nested_str = nested_value if isinstance(nested_value, str) and nested_value else None
                message = payload_dict.get('message') or nested_str or payload_dict.get('error') or fallback_msg

        payload_map = payload_dict or {}
        stacktrace = (
            error_dict.get('stacktrace')
            or error_dict.get('stackTrace')
            or payload_map.get('stacktrace')
            or payload_map.get('stackTrace')
            or response.get('stacktrace')
            or response.get('stackTrace')
            or ''
        )
        screen = error_dict.get('screen') or payload_map.get('screen') or response.get('screen')
        exception_class = _resolve_exception_class(error_identifier, message if isinstance(message, str) else None)

        if exception_class is sel_exceptions.UnexpectedAlertPresentException:
            raise sel_exceptions.UnexpectedAlertPresentException(
                msg=message,
                screen=screen,
                stacktrace=format_stacktrace(stacktrace),
                alert_text=_extract_alert_text(error_dict),
            )
        raise exception_class(msg=message, screen=screen, stacktrace=format_stacktrace(stacktrace))
