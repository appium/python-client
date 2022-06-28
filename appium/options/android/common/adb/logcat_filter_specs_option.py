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

LOGCAT_FILTER_SPECS = 'logcatFilterSpecs'


class LogcatFilterSpecsOption(SupportsCapabilities):
    @property
    def logcat_filter_specs(self) -> Optional[str]:
        """
        Logcat filter format.
        """
        return self.get_capability(LOGCAT_FILTER_SPECS)

    @logcat_filter_specs.setter
    def logcat_filter_specs(self, value: str) -> None:
        """
        Series of tag[:priority] where tag is a log component tag (or * for all)
        and priority is: V Verbose, D Debug, I Info, W Warn, E Error, F Fatal,
        S Silent (supress all output). '' means ':d' and tag by itself means tag:v.
        If not specified on the commandline, filterspec is set from ANDROID_LOG_TAGS.
        If no filterspec is found, filter defaults to '*:I'.
        """
        self.set_capability(LOGCAT_FILTER_SPECS, value)
