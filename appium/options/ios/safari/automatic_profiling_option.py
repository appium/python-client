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

AUTOMATIC_PROFILING = 'safari:automaticProfiling'


class AutomaticProfilingOption(SupportsCapabilities):
    @property
    def automatic_profiling(self) -> Optional[bool]:
        """
        Whether to use automatic profiling.
        """
        return self.get_capability(AUTOMATIC_PROFILING)

    @automatic_profiling.setter
    def automatic_profiling(self, value: bool) -> None:
        """
        This capability instructs Safari to preload the Web Inspector and start
        a Timeline recording in the background prior to returning a newly-created
        window. To view the recording, open the Web Inspector through Safari's
        Develop menu.
        """
        self.set_capability(AUTOMATIC_PROFILING, value)
