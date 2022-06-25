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

from typing import Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

USE_XCTESTRUN_FILE = 'useXctestrunFile'


class UseXctestrunFileOption(SupportsCapabilities):
    @property
    def use_xctestrun_file(self) -> Optional[bool]:
        """
        Whether to use of .xctestrun file to launch WDA.
        """
        return self.get_capability(USE_XCTESTRUN_FILE)

    @use_xctestrun_file.setter
    def use_xctestrun_file(self, value: bool) -> None:
        """
        Use Xctestrun file to launch WDA. It will search for such file in bootstrapPath.
        Expected name of file is WebDriverAgentRunner_iphoneos&lt;sdkVersion&gt;-arm64.xctestrun for
        real device and WebDriverAgentRunner_iphonesimulator&lt;sdkVersion&gt;-x86_64.xctestrun for
        simulator. One can do build-for-testing for WebDriverAgent project for simulator and
        real device and then you will see Product Folder like this and you need to copy content
        of this folder at bootstrapPath location. Since this capability expects that you have
        already built WDA project, it neither checks whether you have necessary dependencies to
        build WDA nor will it try to build project. Defaults to false. Tips: Xcodebuild builds for the
        target platform version. We'd recommend you to build with minimal OS version which you'd
        like to run as the original WDA module. e.g. If you build WDA for 12.2, the module cannot
        run on iOS 11.4 because of loading some module error on simulator. A module built with 11.4
        can work on iOS 12.2. (This is xcodebuild's expected behaviour.)
        """
        self.set_capability(USE_XCTESTRUN_FILE, value)
