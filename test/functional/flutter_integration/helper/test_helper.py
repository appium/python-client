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

import os

from appium import webdriver
from appium.options.flutter_integration.base import FlutterOptions
from appium.webdriver.client_config import AppiumClientConfig
from appium.webdriver.extensions.flutter_integration.flutter_commands import FlutterCommand
from test.helpers.constants import SERVER_URL_BASE

from . import desired_capabilities


class BaseTestCase(object):
    def setup_method(self) -> None:
        platform_name = os.getenv('PLATFORM', 'android').lower()

        # set flutter options
        flutterOptions = FlutterOptions()
        flutterOptions.flutter_system_port = 9999
        flutterOptions.flutter_enable_mock_camera = True
        flutterOptions.flutter_element_wait_timeout = 10000
        flutterOptions.flutter_server_launch_timeout = 120000

        desired_caps = desired_capabilities.get_desired_capabilities(platform_name)

        client_config = AppiumClientConfig(remote_server_addr=SERVER_URL_BASE)
        client_config.timeout = 600

        self.driver = webdriver.Remote(options=flutterOptions.load_capabilities(desired_caps), client_config=client_config)
        self.flutter_command = FlutterCommand(self.driver)

    def teardown_method(self) -> None:  # type: ignore
        if not hasattr(self, 'driver'):
            return
        self.driver.quit()
