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


class PrintPageSourceOnFindFailureOption(SupportsCapabilities):
    PRINT_PAGE_SOURCE_ON_FIND_FAILURE = 'printPageSourceOnFindFailure'

    @property
    def print_page_source_on_find_failure(self) -> Optional[bool]:
        """
        :Returns: Whether the driver should print the page source to the log
        if a find failure occurs.
        """
        return self.get_capability(self.PRINT_PAGE_SOURCE_ON_FIND_FAILURE)

    @print_page_source_on_find_failure.setter
    def print_page_source_on_find_failure(self, value: bool) -> None:
        """
        Set whether the driver should print the page source to the log
        if a find failure occurs.
        """
        self.set_capability(self.PRINT_PAGE_SOURCE_ON_FIND_FAILURE, value)
