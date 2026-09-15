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

KEYCHAINS_EXCLUDE_PATTERNS = 'keychainsExcludePatterns'


class KeychainsExcludePatternsOption(SupportsCapabilities):
    @property
    def keychains_exclude_patterns(self) -> Optional[str]:
        """
        Keychains exclude patterns.
        """
        return self.get_capability(KEYCHAINS_EXCLUDE_PATTERNS)

    @keychains_exclude_patterns.setter
    def keychains_exclude_patterns(self, value: str) -> None:
        """
        This capability accepts comma-separated path patterns,
        which are going to be excluded from keychains restore while
        full reset is being performed on Simulator. It might be
        useful if you want to exclude only particular keychain types
        from being restored, like the applications keychain. This
        feature has no effect on real devices. E.g. "*keychain*.db*"
        to exclude applications keychain from being restored
        """
        self.set_capability(KEYCHAINS_EXCLUDE_PATTERNS, value)
