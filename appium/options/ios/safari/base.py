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

from appium.options.common.common_options import AutomationNameOption
from appium.options.common.base import PLATFORM_NAME, AppiumOptions

from .safari_options import AutomaticInspectionOption
from .safari_options import AutomaticProfilingOption
from .safari_options import DeviceNameOption
from .safari_options import DeviceTypeOption
from .safari_options import DeviceUdidOption
from .safari_options import PlatformBuildVersionOption
from .safari_options import PlatformVersionOption
from .safari_options import UseSimulatorOption
from .safari_options import WebkitWebrtcOption


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
            AutomationNameOption.AUTOMATION_NAME: 'Safari',
        }
