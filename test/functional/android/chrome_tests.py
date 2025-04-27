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

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.client_config import AppiumClientConfig
from appium.webdriver.common.appiumby import AppiumBy
from test.helpers.constants import SERVER_URL_BASE

from .helper.desired_capabilities import get_desired_capabilities


class TestChrome(object):
    def setup_method(self) -> None:
        client_config = AppiumClientConfig(remote_server_addr=SERVER_URL_BASE)
        client_config.timeout = 600
        caps = get_desired_capabilities()
        caps['browserName'] = 'Chrome'
        self.driver = webdriver.Remote(
            SERVER_URL_BASE, options=AppiumOptions().load_capabilities(caps), client_config=client_config
        )

    def teardown_method(self) -> None:
        self.driver.quit()

    def test_find_single_element(self) -> None:
        e = self.driver.find_element(by=AppiumBy.XPATH, value='//body')
        assert e.text == ''

        # Chrome browser's default page
        assert '<html><head></head><body></body></html>' in self.driver.page_source
