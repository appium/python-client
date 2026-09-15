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

APP_ARGUMENTS = 'appArguments'


class AppArgumentsOption(SupportsCapabilities):
    @property
    def app_arguments(self) -> Optional[str]:
        """
        Application arguments string, for example `/?`.
        """
        return self.get_capability(APP_ARGUMENTS)

    @app_arguments.setter
    def app_arguments(self, value: str) -> None:
        """
        Set application arguments string, for example `/argone "/arg two"`.
        Make sure arguments are quoted/escaped properly if necessary:
        https://ss64.com/nt/syntax-esc.html
        """
        self.set_capability(APP_ARGUMENTS, value)
