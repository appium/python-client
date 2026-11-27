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

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from test.helpers.constants import SERVER_URL_BASE
from test.unit.helper.test_helper import appium_command, get_httpretty_request_body


@httpretty.activate
def test_find_element_by_windows_ui_automation():
    caps = {'platformName': 'windows', 'appium:automationName': 'Wincore'}
    httpretty.register_uri(
        httpretty.POST, appium_command('/session'), body=json.dumps({'value': {'sessionId': '123', 'capabilities': caps}})
    )
    driver = webdriver.Remote(SERVER_URL_BASE, options=AppiumOptions().load_capabilities(caps))
    httpretty.register_uri(
        httpretty.POST,
        appium_command('/session/123/element'),
        body='{"value": {"element-6066-11e4-a52e-4f735466cecf": "ok-button"}}',
    )

    condition = "new PropertyCondition(AutomationElement.NameProperty, 'OK')"
    element = driver.find_element(AppiumBy.WINDOWS_UI_AUTOMATION, condition)

    assert element.id == 'ok-button'
    assert get_httpretty_request_body(httpretty.last_request()) == {'using': '-windows uiautomation', 'value': condition}
