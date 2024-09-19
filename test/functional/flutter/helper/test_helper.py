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

import base64
import os

from appium import webdriver
from appium.options.flutter.base import FlutterOptions
from appium.webdriver.extensions.flutter.flutter_commands import FlutterCommand
from test.functional.test_helper import is_ci
from test.helpers.constants import SERVER_URL_BASE

from . import desired_capabilities


class BaseTestCase(object):

    def setup_method(self) -> None:
        platform_name =  os.getenv("PLATFORM", "android").lower()
        
        # set flutter options
        flutterOptions = FlutterOptions()
        flutterOptions.flutter_system_port = 9999
        flutterOptions.flutter_enable_mock_camera = True
        flutterOptions.flutter_element_wait_timeout = 10000
        flutterOptions.flutter_server_launch_timeout = 120000
        
        desired_caps = desired_capabilities.get_desired_capabilities(platform_name)
        self.driver = webdriver.Remote(SERVER_URL_BASE, options=flutterOptions.load_capabilities(desired_caps))
        self.flutter_command = FlutterCommand(self.driver)
        if is_ci():
            self.driver.start_recording_screen()

    def teardown_method(self, method) -> None:  # type: ignore
        if not hasattr(self, 'driver'):
            return

        if is_ci():
            payload = self.driver.stop_recording_screen()
            video_path = os.path.join(os.getcwd(), method.__name__ + '.mp4')
            with open(video_path, 'wb') as fd:
                fd.write(base64.b64decode(payload))
        self.driver.quit()
        
