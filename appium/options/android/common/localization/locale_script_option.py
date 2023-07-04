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


class LocaleScriptOption(SupportsCapabilities):
    LOCALE_SCRIPT = "localeScript"
    locale_script = OptionsDescriptor[Optional[str], str](LOCALE_SCRIPT)
    """
    Gets and Sets canonical name of the locale to be set for the app under test,
    for example zh-Hans-CN.
    See https://developer.android.com/reference/java/util/Locale.html for more details.

    Usage
    -----
    - Get
        - `self.locale_script`
    - Set
        - `self.locale_script` = `value`
    
    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - `None`
    """
