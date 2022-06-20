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

ENABLE_PERFORMANCE_LOGGING = 'enablePerformanceLogging'


class EnablePerformanceLoggingOption(SupportsCapabilities):
    @property
    def enable_performance_logging(self) -> Optional[bool]:
        """
        Whether to enable additional performance logging.
        """
        return self.get_capability(ENABLE_PERFORMANCE_LOGGING)

    @enable_performance_logging.setter
    def enable_performance_logging(self, value: bool) -> None:
        """
        Set whether to enable additional performance logging.
        """
        self.set_capability(ENABLE_PERFORMANCE_LOGGING, value)
