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

from os import PathLike, fspath

from appium.options.common.supports_capabilities import SupportsCapabilities

LOG_FILE = 'logFile'


class LogFileOption(SupportsCapabilities):
    @property
    def log_file(self) -> str | bool | None:
        """
        File path or boolean flag controlling session log mirroring.
        """
        return self.get_capability(LOG_FILE)

    @log_file.setter
    def log_file(self, value: str | PathLike[str] | bool) -> None:
        """
        Mirror the driver session log to a file. Pass True for a timestamped default
        path, a directory path ending in a separator, or an explicit file path.
        """
        self.set_capability(LOG_FILE, value if isinstance(value, bool) else fspath(value))
