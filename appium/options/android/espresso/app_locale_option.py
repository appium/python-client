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

from typing import Dict, Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

APP_LOCALE = 'appLocale'


class AppLocaleOption(SupportsCapabilities):
    @property
    def app_locale(self) -> Optional[Dict[str, str]]:
        """
        Locale for the app under test.
        """
        return self.get_capability(APP_LOCALE)

    @app_locale.setter
    def app_locale(self, value: Dict[str, str]) -> None:
        """
        Sets the locale for the app under test. The main difference between this option
        and the above ones is that this option only changes the locale for the application
        under test and does not affect other parts of the system. Also, it only uses
        public APIs for its purpose. See
        https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers to get the
        list of available language abbreviations.
        Example: {"language": "zh", "country": "CN", "variant": "Hans"}.
        """
        self.set_capability(APP_LOCALE, value)
