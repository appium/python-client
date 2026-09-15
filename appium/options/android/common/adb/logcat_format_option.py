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

LOGCAT_FORMAT = 'logcatFormat'


class LogcatFormatOption(SupportsCapabilities):
    @property
    def logcat_format(self) -> Optional[str]:
        """
        Log print format.
        """
        return self.get_capability(LOGCAT_FORMAT)

    @logcat_format.setter
    def logcat_format(self, value: str) -> None:
        """
        The log print format, where format is one of: brief process tag thread raw time
        threadtime long. threadtime is the default value.
        """
        self.set_capability(LOGCAT_FORMAT, value)
