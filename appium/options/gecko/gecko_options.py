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

from typing import Any, Dict, Optional

from appium.options.base_options_descriptor import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities


class AndroidStorageOption(SupportsCapabilities):
    ANDROID_STORAGE = "androidStorage"
    android_storage = OptionsDescriptor[Optional[str], str](ANDROID_STORAGE)
    """
    Gets and Sets Current storge type
    See https://firefox-source-docs.mozilla.org/testing/geckodriver
    /Flags.html#code-android-storage-var-android-storage-var-code

    Usage
    -----
    - Get
        - `self.android_storage`
    - Set
        - `self.android_storage` = `value`

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


class FirefoxOptionsOption(SupportsCapabilities):
    FIREFOX_OPTIONS = "moz:firefoxOptions"
    firefox_options = OptionsDescriptor[Optional[Dict[str, Any]], Dict[str, Any]](FIREFOX_OPTIONS)
    """
    Gets and Sets Firefox mapping
    See https://developer.mozilla.org/en-US/docs/Web/WebDriver/Capabilities/firefoxOptions

    Usage
    -----
    - Get
        - `self.firefox_options`
    - Set
        - `self.firefox_options` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, Any]`

    Returns
    -------
    - Get
        - `Optional[Dict[str, Any]]`
    - Set
        - `None`
    """


class MarionettePortOption(SupportsCapabilities):
    MARIONETTE_PORT = "marionettePort"
    marionette_port = OptionsDescriptor[Optional[int], int](MARIONETTE_PORT)
    """
    Selects the port for Geckodriver’s connection to the Marionette
    remote protocol. The existing Firefox instance must have Marionette
    enabled. To enable the remote protocol in Firefox, you can pass the
    -marionette flag. Unless the marionette.port preference has been
    user-set, Marionette will listen on port 2828, which is the default
    value for this capability.

    Usage
    -----
    - Get
        - `self.marionette_port`
    - Set
        - `self.marionette_port` = `value`
    
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


class VerbosityOption(SupportsCapabilities):
    VERBOSITY = "verbosity"
    verbosity = OptionsDescriptor[Optional[str], str](VERBOSITY)
    """
    Sets and Gets the  verbosity level of driver logging.
    The verbosity level of driver logging.
    By default, minimum verbosity is applied.
    Either 'debug' or 'trace'.

    Usage
    -----
    - Get
        - `self.verbosity`
    - Set
        - `self.verbosity` = `value`
    
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
