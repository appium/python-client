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

import time
from typing import TYPE_CHECKING, Generator

import pytest

from appium import webdriver
from appium.webdriver.client_config import AppiumClientConfig
from test.helpers.constants import SERVER_URL_BASE

from .helper.options import make_options

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


@pytest.fixture
def driver() -> Generator['WebDriver', None, None]:
    """Create and configure Safari driver for testing."""
    options = make_options()
    options.bundle_id = 'com.apple.mobilesafari'
    options.native_web_tap = True
    options.safari_ignore_fraud_warning = True
    options.webview_connect_timeout = 100000

    client_config = AppiumClientConfig(remote_server_addr=SERVER_URL_BASE)
    client_config.timeout = 600
    driver = webdriver.Remote(options=options, client_config=client_config)

    # Fresh iOS 17.4 simulator may not show up the webview context with "safari"
    # after a fresh simlator instance creation.
    # Re-launch the process could be a workaround in my debugging.
    driver.terminate_app('com.apple.mobilesafari')
    driver.activate_app('com.apple.mobilesafari')

    yield driver

    driver.quit()


def test_context(driver: 'WebDriver') -> None:
    """Test Safari context switching."""
    contexts = driver.contexts
    assert 'NATIVE_APP' == contexts[0]
    assert contexts[1].startswith('WEBVIEW_')
    driver.switch_to.context(contexts[1])
    assert 'WEBVIEW_' in driver.current_context


def test_navigation(driver: 'WebDriver') -> None:
    """Test Safari navigation to Google."""
    contexts = driver.contexts
    for context in contexts:
        if context.startswith('WEBVIEW_'):
            driver.switch_to.context(context)
            break
    else:
        pytest.fail('Could not set WEBVIEW context')

    driver.get('http://google.com')
    for _ in range(5):
        time.sleep(0.5)
        if 'Google' == driver.title:
            return
    else:
        pytest.fail('The title was wrong')
