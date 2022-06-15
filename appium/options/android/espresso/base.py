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

from appium.options.common.app_option import AppOption
from appium.options.common.auto_web_view_option import AutoWebViewOption
from appium.options.common.automation_name_option import AUTOMATION_NAME
from appium.options.common.base import PLATFORM_NAME, AppiumOptions
from appium.options.common.device_name_option import DeviceNameOption
from appium.options.common.is_headless_option import IsHeadlessOption
from appium.options.common.language_option import LanguageOption
from appium.options.common.locale_option import LocaleOption
from appium.options.common.orientation_option import OrientationOption
from appium.options.common.skip_log_capture_option import SkipLogCaptureOption
from appium.options.common.udid_option import UdidOption


class EspressoOptions(
    AppiumOptions,
    AppOption,
    OrientationOption,
    UdidOption,
    LanguageOption,
    LocaleOption,
    IsHeadlessOption,
    SkipLogCaptureOption,
    AutoWebViewOption,
    DeviceNameOption,
):
    @property
    def default_capabilities(self) -> Dict:
        return {
            AUTOMATION_NAME: 'Espresso',
            PLATFORM_NAME: 'Android',
        }
