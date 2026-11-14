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

import httpretty
import pytest
from selenium.common import exceptions
from selenium.webdriver.common.by import By

from appium.common.exceptions import InvalidSwitchToTargetException, NoSuchContextException
from appium.webdriver.errorhandler import MobileErrorHandler
from test.unit.helper.test_helper import android_w3c_driver, appium_command


@pytest.mark.parametrize(
    ('error', 'message', 'expected'),
    [
        ('no such element', 'Missing element', exceptions.NoSuchElementException),
        ('detached shadow root', 'Detached', exceptions.DetachedShadowRootException),
        ('unknown command', 'Unknown command', exceptions.UnknownMethodException),
        ('unknown method', 'Unknown method', exceptions.UnknownMethodException),
        ('unsupported operation', 'Unsupported', exceptions.UnknownMethodException),
        ('unknown error', 'No such context found.', NoSuchContextException),
        ('unknown error', 'That command could not be executed in the current context.', InvalidSwitchToTargetException),
        ('invalid argument', 'No such context found.', exceptions.InvalidArgumentException),
        ('unknown error', 'Other error', exceptions.WebDriverException),
    ],
)
def test_w3c_exception_mapping(error, message, expected):
    response = {
        'status': 500,
        'value': json.dumps(
            {
                'value': {
                    'error': error,
                    'message': message,
                    'stacktrace': 'line1\nline2',
                }
            }
        ),
    }
    with pytest.raises(expected) as caught:
        MobileErrorHandler().check_response(response)
    assert type(caught.value) is expected
    assert caught.value.msg.startswith(message)
    assert caught.value.stacktrace == ['line1', 'line2']


@pytest.mark.parametrize('data', [{'text': 'Allow location?'}, {}])
@httpretty.activate
def test_driver_unexpected_alert_text(data):
    driver = android_w3c_driver()
    httpretty.register_uri(
        httpretty.POST,
        appium_command('/session/1234567890/element'),
        status=500,
        body=json.dumps(
            {
                'value': {
                    'error': 'unexpected alert open',
                    'message': 'Blocked',
                    'stacktrace': '',
                    'data': data,
                }
            }
        ),
    )
    with pytest.raises(exceptions.UnexpectedAlertPresentException) as caught:
        driver.find_element(By.ID, 'button')
    assert caught.value.alert_text == data.get('text')


@pytest.mark.parametrize(
    'response',
    [
        {'value': None},
        {'value': {'error': 'timeout', 'message': 'User script result'}},
        {'status': 7, 'value': {'message': 'Legacy error'}},
        {'status': 500, 'value': '{"status": 7, "value": {"message": "Legacy error"}}'},
    ],
)
def test_non_w3c_errors_are_not_interpreted(response):
    MobileErrorHandler().check_response(response)
