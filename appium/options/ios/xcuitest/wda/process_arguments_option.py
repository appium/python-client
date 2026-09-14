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

from typing import Dict, List, Optional, Union

from appium.options.common.supports_capabilities import SupportsCapabilities

PROCESS_ARGUMENTS = 'processArguments'


class ProcessArgumentsOption(SupportsCapabilities):
    @property
    def process_arguments(self) -> Optional[Dict[str, Union[List[str], Dict[str, str]]]]:
        """
        Command line arguments and/or environment variables of the application under test.
        """
        return self.get_capability(PROCESS_ARGUMENTS)

    @process_arguments.setter
    def process_arguments(self, value: Dict[str, Union[List[str], Dict[str, str]]]) -> None:
        """
        Provides process arguments and environment which will be sent
        to the WebDriverAgent server. Acceptable dictionary keys are 'env'
        and 'args'. The value of 'args' should be a list of app command line
        arguments represented as strings and the value of 'env' is expected to
        be a dictionary of environment variable names and their values (also strings).
        """
        self.set_capability(PROCESS_ARGUMENTS, value)
