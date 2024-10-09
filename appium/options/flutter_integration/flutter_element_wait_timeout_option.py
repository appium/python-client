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

FLUTTER_ELEMENT_WAIT_TIMEOUT = 'flutterElementWaitTimeout'


class FlutterElementWaitTimeOutOption(SupportsCapabilities):
    @property
    def flutter_element_wait_timeout(self) -> Optional[timedelta]:
        """
        Maximum timeout to wait for element for Flutter integration test

        Returns:
            Optional[timedelta]: The timeout value as a `timedelta` object if set, or `None` if the timeout is not defined.
        """
        return self.get_capability(FLUTTER_ELEMENT_WAIT_TIMEOUT)

    @flutter_element_wait_timeout.setter
    def flutter_element_wait_timeout(self, value: Union[timedelta, int]) -> None:
        """
        Sets the maximum timeout to wait for a Flutter element in an integration test.
        Default timeout is 5000ms

        Args:
            value (Union[timedelta, int]): The timeout value, either as a `timedelta` object or an integer in milliseconds.
                If provided as a `timedelta`, it will be converted to milliseconds.
        """
        self.set_capability(
            FLUTTER_ELEMENT_WAIT_TIMEOUT,
            (int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value),
        )
