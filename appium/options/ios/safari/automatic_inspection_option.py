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

AUTOMATIC_INSPECTION = 'safari:automaticInspection'


class AutomaticInspectionOption(SupportsCapabilities):
    @property
    def automatic_inspection(self) -> Optional[bool]:
        """
        Whether to use automatic inspection.
        """
        return self.get_capability(AUTOMATIC_INSPECTION)

    @automatic_inspection.setter
    def automatic_inspection(self, value: bool) -> None:
        """
        This capability instructs Safari to preload the Web Inspector and JavaScript
        debugger in the background prior to returning a newly-created window.
        To pause the test's execution in JavaScript and bring up Web Inspector's
        Debugger tab, you can simply evaluate a debugger statement in the test page.
        """
        self.set_capability(AUTOMATIC_INSPECTION, value)
