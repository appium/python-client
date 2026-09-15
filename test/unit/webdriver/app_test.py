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

from appium.webdriver.applicationstate import ApplicationState
from appium.webdriver.webdriver import WebDriver
from test.unit.helper.test_helper import android_w3c_driver, appium_command, get_httpretty_request_body, ios_w3c_driver


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_install_app(driver_func):
    driver = driver_func()
    httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": ""}')
    result = driver.install_app('path/to/app')

    assert {
        'args': [{'app': 'path/to/app', 'appPath': 'path/to/app'}],
        'script': 'mobile: installApp',
    } == get_httpretty_request_body(httpretty.last_request())
    assert isinstance(result, WebDriver)


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_remove_app(driver_func):
    driver = android_w3c_driver()
    httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": ""}')
    result = driver.remove_app('com.app.id')

    assert {
        'args': [{'appId': 'com.app.id', 'bundleId': 'com.app.id'}],
        'script': 'mobile: removeApp',
    } == get_httpretty_request_body(httpretty.last_request())
    assert isinstance(result, WebDriver)


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_app_installed(driver_func):
    driver = driver_func()
    httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": true}')
    result = driver.is_app_installed('com.app.id')

    assert {
        'args': [{'appId': 'com.app.id', 'bundleId': 'com.app.id'}],
        'script': 'mobile: isAppInstalled',
    } == get_httpretty_request_body(httpretty.last_request())
    assert result is True


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_terminate_app(driver_func):
    driver = driver_func()
    httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": true}')
    result = driver.terminate_app('com.app.id')

    assert {
        'args': [{'appId': 'com.app.id', 'bundleId': 'com.app.id'}],
        'script': 'mobile: terminateApp',
    } == get_httpretty_request_body(httpretty.last_request())
    assert result is True


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_activate_app(driver_func):
    driver = driver_func()
    httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": ""}')
    result = driver.activate_app('com.app.id')

    assert {
        'args': [{'appId': 'com.app.id', 'bundleId': 'com.app.id'}],
        'script': 'mobile: activateApp',
    } == get_httpretty_request_body(httpretty.last_request())
    assert isinstance(result, WebDriver)


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_background_app(driver_func):
    driver = driver_func()
    httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": ""}')
    result = driver.background_app(0)

    assert {'args': [{'seconds': 0}], 'script': 'mobile: backgroundApp'} == get_httpretty_request_body(httpretty.last_request())
    assert isinstance(result, WebDriver)


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_query_app_state(driver_func):
    driver = driver_func()
    httpretty.register_uri(httpretty.POST, appium_command('/session/1234567890/execute/sync'), body='{"value": 3}')
    result = driver.query_app_state('com.app.id')

    assert {
        'args': [{'appId': 'com.app.id', 'bundleId': 'com.app.id'}],
        'script': 'mobile: queryAppState',
    } == get_httpretty_request_body(httpretty.last_request())
    assert result is ApplicationState.RUNNING_IN_BACKGROUND


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_app_strings(driver_func):
    driver = driver_func()
    httpretty.register_uri(
        httpretty.POST,
        appium_command('/session/1234567890/execute/sync'),
        body='{"value": {"monkey_wipe_data": "You can\'t wipe my data, you are a monkey!"} }',
    )
    result = driver.app_strings()

    assert {'args': [{}], 'script': 'mobile: getAppStrings'} == get_httpretty_request_body(httpretty.last_request())
    assert "You can't wipe my data, you are a monkey!" == result['monkey_wipe_data'], result


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_app_strings_with_lang(driver_func):
    driver = driver_func()
    httpretty.register_uri(
        httpretty.POST,
        appium_command('/session/1234567890/execute/sync'),
        body='{"value": {"monkey_wipe_data": "You can\'t wipe my data, you are a monkey!"} }',
    )
    result = driver.app_strings('en')

    assert {'args': [{'language': 'en'}], 'script': 'mobile: getAppStrings'} == get_httpretty_request_body(
        httpretty.last_request()
    )
    assert "You can't wipe my data, you are a monkey!" == result['monkey_wipe_data'], result


@pytest.mark.parametrize('driver_func', [android_w3c_driver, ios_w3c_driver])
@httpretty.activate
def test_app_strings_with_lang_and_file(driver_func):
    driver = driver_func()
    httpretty.register_uri(
        httpretty.POST,
        appium_command('/session/1234567890/execute/sync'),
        body='{"value": {"monkey_wipe_data": "You can\'t wipe my data, you are a monkey!"} }',
    )
    result = driver.app_strings('en', 'some_file')

    assert {
        'args': [{'language': 'en', 'stringFile': 'some_file'}],
        'script': 'mobile: getAppStrings',
    } == get_httpretty_request_body(httpretty.last_request())
    assert "You can't wipe my data, you are a monkey!" == result['monkey_wipe_data'], result
