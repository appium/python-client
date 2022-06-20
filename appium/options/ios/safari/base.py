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
from appium.options.common.base import PLATFORM_NAME, AppiumOptions

from .automatic_inspection_option import AutomaticInspectionOption
from .automatic_profiling_option import AutomaticProfilingOption
from .device_name_option import DeviceNameOption
from .device_type_option import DeviceTypeOption
from .device_udid_option import DeviceUdidOption
from .platform_build_version_option import PlatformBuildVersionOption
from .platform_version_option import PlatformVersionOption
from .use_simulator_option import UseSimulatorOption
from .webkit_webrtc_option import WebkitWebrtcOption


class SafariOptions(
    AppiumOptions,
    AutomaticInspectionOption,
    AutomaticProfilingOption,
    DeviceNameOption,
    DeviceTypeOption,
    DeviceUdidOption,
    PlatformBuildVersionOption,
    PlatformVersionOption,
    UseSimulatorOption,
    WebkitWebrtcOption,
):
    @property
    def default_capabilities(self) -> Dict:
        return {
            PLATFORM_NAME: 'iOS',
            AUTOMATION_NAME: 'Safari',
        }
