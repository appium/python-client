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

from .supports_capabilities import SupportsCapabilities

APP = 'app'


class AppOption(SupportsCapabilities):
    @property
    def app(self) -> Optional[str]:
        """
        String representing app location.
        """
        return self.get_capability(APP)

    @app.setter
    def app(self, value: str) -> None:
        """
        Set the absolute local path for the location of the App.
        The app must be located on the same machine where Appium
        server is running.
        Could also be a valid URL.
        """
        self.set_capability(APP, value)
