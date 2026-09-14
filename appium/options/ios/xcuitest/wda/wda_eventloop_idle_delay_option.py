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

from datetime import timedelta
from typing import Optional, Union

from appium.options.common.supports_capabilities import SupportsCapabilities

WDA_EVENTLOOP_IDLE_DELAY = 'wdaEventloopIdleDelay'


class WdaEventloopIdleDelayOption(SupportsCapabilities):
    @property
    def wda_eventloop_idle_delay(self) -> Optional[timedelta]:
        """
        Event loop idle delay.
        """
        value = self.get_capability(WDA_EVENTLOOP_IDLE_DELAY)
        return None if value is None else timedelta(seconds=value)

    @wda_eventloop_idle_delay.setter
    def wda_eventloop_idle_delay(self, value: Union[timedelta, float]) -> None:
        """
        Delays the invocation of -[XCUIApplicationProcess setEventLoopHasIdled:] by the
        duration specified with this capability. This can help quiescence apps
        that fail to do so for no obvious reason (and creating a session fails for
        that reason). This increases the time for session creation
        because -[XCUIApplicationProcess setEventLoopHasIdled:] is called multiple times.
        If you enable this capability start with at least 3 seconds and try increasing it,
        if creating the session still fails. Defaults to 0.
        """
        self.set_capability(WDA_EVENTLOOP_IDLE_DELAY, value.total_seconds() if isinstance(value, timedelta) else value)
