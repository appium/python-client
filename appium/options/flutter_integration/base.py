# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import Dict

from appium.options.common.automation_name_option import AUTOMATION_NAME
from appium.options.common.base import AppiumOptions
from appium.options.flutter_integration.flutter_element_wait_timeout_option import FlutterElementWaitTimeOutOption
from appium.options.flutter_integration.flutter_enable_mock_camera_option import FlutterEnableMockCameraOption
from appium.options.flutter_integration.flutter_server_launch_timeout_option import FlutterServerLaunchTimeOutOption
from appium.options.flutter_integration.flutter_system_port_option import FlutterSystemPortOption


class FlutterOptions(
    AppiumOptions,
    FlutterElementWaitTimeOutOption,
    FlutterEnableMockCameraOption,
    FlutterServerLaunchTimeOutOption,
    FlutterSystemPortOption,
):
    @property
    def default_capabilities(self) -> Dict:
        return {
            AUTOMATION_NAME: 'FlutterIntegration',
        }
