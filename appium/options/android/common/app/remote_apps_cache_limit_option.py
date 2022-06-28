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

REMOTE_APPS_CACHE_LIMIT = 'remoteAppsCacheLimit'


class RemoteAppsCacheLimitOption(SupportsCapabilities):
    @property
    def remote_apps_cache_limit(self) -> Optional[int]:
        """
        Maximum amount of apps that could be cached on the remote device.
        """
        return self.get_capability(REMOTE_APPS_CACHE_LIMIT)

    @remote_apps_cache_limit.setter
    def remote_apps_cache_limit(self, value: int) -> None:
        """
        Set the maximum amount of application packages to be cached on the device under test.
        This is needed for devices that don't support streamed installs (Android 7 and below),
        because ADB must push app packages to the device first in order to install them,
        which takes some time. Setting this capability to zero disables apps caching.
        10 by default.
        """
        self.set_capability(REMOTE_APPS_CACHE_LIMIT, value)
