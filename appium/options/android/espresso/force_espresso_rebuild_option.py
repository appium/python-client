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


class ForceEspressoRebuildOption(SupportsCapabilities):
    FORCE_ESPRESSO_REBUILD = "forceEspressoRebuild"
    force_espresso_rebuild = OptionsDescriptor[Optional[bool], bool](FORCE_ESPRESSO_REBUILD)
    """
    Gets and Sets Whether to always enforce Espresso server rebuild (true).
    By default, Espresso caches the already built server apk and only rebuilds
    it when it is necessary, because rebuilding process needs extra time.
    false by default.

    Usage
    -----
    - Get
        - `self.force_espresso_rebuild`
    - Set
        - `self.force_espresso_rebuild` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """
