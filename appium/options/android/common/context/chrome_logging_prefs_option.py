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

from typing import Any, Dict, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

CHROME_LOGGING_PREFS = 'chromeLoggingPrefs'


class ChromeLoggingPrefsOption(SupportsCapabilities):
    @property
    def chrome_logging_prefs(self) -> Optional[Dict[str, Any]]:
        """
        Chrome logging preferences.
        """
        return self.get_capability(CHROME_LOGGING_PREFS)

    @chrome_logging_prefs.setter
    def chrome_logging_prefs(self, value: Dict[str, Any]) -> None:
        """
        Chrome logging preferences mapping. Basically the same as
        [goog:loggingPrefs](https://newbedev.com/
        getting-console-log-output-from-chrome-with-selenium-python-api-bindings).
        It is set to {"browser": "ALL"} by default.
        """
        self.set_capability(CHROME_LOGGING_PREFS, value)
