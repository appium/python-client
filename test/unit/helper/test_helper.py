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

import unittest
import httpretty
import json

from appium import webdriver


class TestHelper():

    @staticmethod
    def mock_android_driver():
        """
        Return a driver which is generated a mock response

        :return: An instance of WebDriver
        :rtype: WebDriver
        """

        response_body_json = json.dumps(
            {
                'value': {
                    'sessionId': '1234567890',
                    'capabilities': {
                        'platform': 'LINUX',
                        'desired': {
                            'platformName': 'Android',
                            'automationName': 'uiautomator2',
                            'platformVersion': '7.1.1',
                            'deviceName': 'Android Emulator',
                            'app': '/test/apps/ApiDemos-debug.apk',
                        },
                        'platformName': 'Android',
                        'automationName': 'uiautomator2',
                        'platformVersion': '7.1.1',
                        'deviceName': 'emulator-5554',
                        'app': '/test/apps/ApiDemos-debug.apk',
                        'deviceUDID': 'emulator-5554',
                        'appPackage': 'com.example.android.apis',
                        'appWaitPackage': 'com.example.android.apis',
                        'appActivity': 'com.example.android.apis.ApiDemos',
                        'appWaitActivity': 'com.example.android.apis.ApiDemos'
                    }
                }
            }
        )

        httpretty.register_uri(
            httpretty.POST,
            'http://localhost:4723/wd/hub/session',
            body = response_body_json
        )

        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',
            'app': 'path/to/app',
            'automationName': 'UIAutomator2'
        }
        driver = webdriver.Remote(
            'http://localhost:4723/wd/hub',
            desired_caps
        )
        return driver
