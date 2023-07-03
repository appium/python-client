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

import json
from datetime import timedelta
from typing import Any, Dict, Optional, Union

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities
from appium.options.transformers import transform_duration_get, transform_duration_set


class ActivityOptionsOption(SupportsCapabilities):
    ACTIVITY_OPTIONS = "activityOptions"
    activity_options = OptionsDescriptor[Optional[Dict], Dict](ACTIVITY_OPTIONS)
    """
    The mapping of custom options for the main app activity that is going to
    be started. Check
    https://github.com/appium/appium-espresso-driver#activity-options
    for more details.

    Usage
    -----
    - Get
        - `self.activity_options`
    - Set
        - `self.activity_options` = `value`
    
    Parameters
    ----------
    `value`: `Dict`

    Returns
    -------
    - Get
        - `Optional[Dict]`
    - Set
        - `None`
    """


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


class EspressoBuildConfigOption(SupportsCapabilities):
    ESPRESSO_BUILD_CONFIG = "espressoBuildConfig"

    @staticmethod
    def transform_get(value: Any) -> Any:
        try:
            return json.loads(value)
        except Exception:
            return value

    @staticmethod
    def transform_set(value: Union[str, Any]) -> str:
        return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)

    espresso_build_config = OptionsDescriptor[Optional[Union[Dict[str, Any], str]], Union[Dict[str, Any], str]]
    (ESPRESSO_BUILD_CONFIG, transform_get, transform_set)
    """
    This config allows to customize several important properties of
    Espresso server. Refer to
    https://github.com/appium/appium-espresso-driver#espresso-build-config
    for more information on how to properly construct such config.

    Usage
    -----
    - Get
        - `self.espresso_build_config`
    - Set
        - `self.espresso_build_config` = `value`
    
    Parameters
    ----------
    `value`: `Union[Dict[str, Any], str]`

    Returns
    -------
    - Get
        - `Optional[Union[Dict[str, Any], str]]`
    - Set
        - `None`
    """


class EspressoServerLaunchTimeoutOption(SupportsCapabilities):
    ESPRESSO_SERVER_LAUNCH_TIMEOUT = "espressoServerLaunchTimeout"
    espresso_server_launch_timeout = OptionsDescriptor[Optional[timedelta], Union[timedelta, int]]
    (ESPRESSO_SERVER_LAUNCH_TIMEOUT, transform_duration_get, transform_duration_set)
    """Gets and Sets the maximum timeout to wait util Espresso  is listening on the device.
    45000 ms by default

    Usage
    -----
    - Get
        - `self.espresso_server_launch_timeout`
    - Set
        - `self.espresso_server_launch_timeout` = `value`

    Parameters
    ----------
    `value`: `Union[timedelta, int]`

    Returns
    -------
    - Get
        - `Optional[timedelta]`
    - Set
        - `None`
    """


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


class IntentOptionsOption(SupportsCapabilities):
    INTENT_OPTIONS = "intentOptions"
    intent_options = OptionsDescriptor[Optional[Dict[str, Any]], Dict[str, Any]](INTENT_OPTIONS)
    """
    The mapping of custom options for the intent that is going to be passed
    to the main app activity. Check
    https://github.com/appium/appium-espresso-driver#intent-options
    for more details.

    Usage
    -----
    - Get
        - `self.intent_options`
    - Set
        - `self.intent_options` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, Any]`

    Returns
    -------
    - Get
        - `Dict[str, Any]`
    - Set
        - `None`
    """


class ShowGradleLogOption(SupportsCapabilities):
    SHOW_GRADLE_LOG = "showGradleLog"
    show_gradle_log = OptionsDescriptor[Optional[bool], bool](SHOW_GRADLE_LOG)
    """
    Whether to include Gradle log to the regular server logs while
    building Espresso server. false by default.

    Usage
    -----
    - Get
        - `self.show_gradle_log`
    - Set
        - `self.show_gradle_log` = `value`
    
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
