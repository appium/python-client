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


FLUTTER_SERVER_LAUNCH_TIMEOUT= 'flutterServerLaunchTimeout'


class FlutterServerLaunchTimeOutOption(SupportsCapabilities):
    
    @property
    def flutter_server_launch_timeout(self) -> Optional[int]:
        return self.get_capability(FLUTTER_SERVER_LAUNCH_TIMEOUT)

    @flutter_server_launch_timeout.setter
    def flutter_server_launch_timeout(self, time_in_millis: int) -> None:
        self.set_capability(FLUTTER_SERVER_LAUNCH_TIMEOUT, time_in_millis)