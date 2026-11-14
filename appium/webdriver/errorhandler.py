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
from typing import Any

import selenium.common.exceptions as sel_exceptions
from selenium.webdriver.remote import errorhandler

import appium.common.exceptions as appium_exceptions


class MobileErrorHandler(errorhandler.ErrorHandler):
    def check_response(self, response: dict[str, Any]) -> None:
        """Handle W3C errors, retaining Appium-specific exception mappings."""
        payload = response.get('value', '')
        if isinstance(payload, dict):
            payload_dict = payload
        else:
            try:
                payload_dict = json.loads(payload)
            except (json.JSONDecodeError, TypeError):
                return
            if not isinstance(payload_dict, dict):
                return
        value = payload_dict.get('value')
        if not isinstance(value, dict):
            return
        error = value.get('error')
        if not isinstance(error, str) or not error:
            return

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
