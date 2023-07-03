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

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities


class UserProfileOption(SupportsCapabilities):
    USER_PROFILE = "userProfile"
    user_profile = OptionsDescriptor[Optional[int], int](USER_PROFILE)
    """
    Integer identifier of a user profile. By default, the app under test is
    installed for the currently active user, but in case it is necessary to
    test how the app performs while being installed for a user profile,
    which is different from the current one, this capability might
    come in handy.

    Usage
    -----
    - Get
        - `self.user_profile`
    - Set
        - `self.user_profile` = `value`
    
    Parameters
    ----------
    `value`: `int`

    Returns
    -------
    - Get
        - `Optional[int]`
    - Set
        - `None`
    """
