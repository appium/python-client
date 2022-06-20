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

BUNDLE_ID = 'bundleId'


class BundleIdOption(SupportsCapabilities):
    @property
    def bundle_id(self) -> Optional[str]:
        """
        The bundle identifier of the application to automate.
        """
        return self.get_capability(BUNDLE_ID)

    @bundle_id.setter
    def bundle_id(self, value: str) -> None:
        """
        Set the bundle identifier of the application to automate, for example
        com.apple.TextEdit. This is an optional capability. If it is not provided
        then the session will be started without an application under test
        (actually, it will be Finder). If the application with the given
        identifier is not installed then an error will be thrown on session
        startup. If the application is already running then it will be moved to
        the foreground.
        """
        self.set_capability(BUNDLE_ID, value)
