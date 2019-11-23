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

# :return: A string of test URL
SERVER_URL_BASE = 'http://localhost:4723/wd/hub'


def appium_command(command):
    """Return a command of Appium

    Returns:
        str: A string of command URL
    """
    return '{}{}'.format(SERVER_URL_BASE, command)


def android_w3c_driver():
    """Return a W3C driver which is generated by a mock response for Android

    Returns:
        `webdriver.webdriver.WebDriver`: An instance of WebDriver
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
                    'appPackage': 'io.appium.android.apis',
                    'appWaitPackage': 'io.appium.android.apis',
                    'appActivity': 'io.appium.android.apis.ApiDemos',
                    'appWaitActivity': 'io.appium.android.apis.ApiDemos'
                }
            }
        }
    )

    httpretty.register_uri(
        httpretty.POST,
        appium_command('/session'),
        body=response_body_json
    )

    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Android Emulator',
        'app': 'path/to/app',
        'automationName': 'UIAutomator2'
    }

    driver = webdriver.Remote(
        SERVER_URL_BASE,
        desired_caps
    )
    return driver


def ios_w3c_driver():
    """Return a W3C driver which is generated by a mock response for iOS

    Returns:
        `webdriver.webdriver.WebDriver`: An instance of WebDriver
    """

    response_body_json = json.dumps(
        {
            'value': {
                'sessionId': '1234567890',
                'capabilities': {
                    'device': 'iphone',
                    'browserName': 'UICatalog',
                    'sdkVersion': '11.4',
                    'CFBundleIdentifier': 'com.example.apple-samplecode.UICatalog'
                }
            }
        }
    )

    httpretty.register_uri(
        httpretty.POST,
        appium_command('/session'),
        body=response_body_json
    )

    desired_caps = {
        'platformName': 'iOS',
        'deviceName': 'iPhone Simulator',
        'app': 'path/to/app',
        'automationName': 'XCUITest'
    }

    driver = webdriver.Remote(
        SERVER_URL_BASE,
        desired_caps
    )
    return driver


def get_httpretty_request_body(request):
    """Returns utf-8 decoded request body"""
    return json.loads(request.body.decode('utf-8'))
