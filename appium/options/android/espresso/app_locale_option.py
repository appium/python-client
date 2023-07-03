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

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities


class AppLocaleOption(SupportsCapabilities):
    APP_LOCALE = "appLocale"
    app_locale = OptionsDescriptor[Optional[Dict[str, str]], Dict[str, str]](APP_LOCALE)
    """
    Sets the locale for the app under test. The main difference between this option
    and the above ones is that this option only changes the locale for the application
    under test and does not affect other parts of the system. Also, it only uses
    public APIs for its purpose. See
    https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers to get the
    list of available language abbreviations.
    Example: {"language": "zh", "country": "CN", "variant": "Hans"}.

    Usage
    -----
    - Get
        - `self.app_locale`
    - Set
        - `self.app_locale` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, str]`

    Returns
    -------
    - Get
        - `Optional[Dict[str, str]]`
    - Set
        - `None`
    """
