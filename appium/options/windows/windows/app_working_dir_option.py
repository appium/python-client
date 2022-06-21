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

APP_WORKING_DIR = 'appWorkingDir'


class AppWorkingDirOption(SupportsCapabilities):
    @property
    def app_working_dir(self) -> Optional[str]:
        """
        Full path to the folder, which is going to be set as the working
        dir for the application under test.
        """
        return self.get_capability(APP_WORKING_DIR)

    @app_working_dir.setter
    def app_working_dir(self, value: str) -> None:
        """
        Set the full path to the folder, which is going to be set as the working
        dir for the application under test. This is only applicable for classic apps.
        """
        self.set_capability(APP_WORKING_DIR, value)
