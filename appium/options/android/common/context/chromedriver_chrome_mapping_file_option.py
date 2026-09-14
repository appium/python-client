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

CHROMEDRIVER_CHROME_MAPPING_FILE = 'chromedriverChromeMappingFile'


class ChromedriverChromeMappingFileOption(SupportsCapabilities):
    @property
    def chromedriver_chrome_mapping_file(self) -> Optional[str]:
        """
        Full path to the chromedrivers mapping file is located.
        """
        return self.get_capability(CHROMEDRIVER_CHROME_MAPPING_FILE)

    @chromedriver_chrome_mapping_file.setter
    def chromedriver_chrome_mapping_file(self, value: str) -> None:
        """
        Full path to the chromedrivers mapping file. This file is used to statically
        map webview/browser versions to the chromedriver versions that are capable
        of automating them. Read [Automatic Chromedriver Discovery](https://github.com/
        appium/appium/blob/master/docs/en/writing-running-appium/web/
        chromedriver.md#automatic-discovery-of-compatible-chromedriver)
        article for more details.
        """
        self.set_capability(CHROMEDRIVER_CHROME_MAPPING_FILE, value)
