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

from typing import Any, TypeVar

from appium.options.common.supports_capabilities import SupportsCapabilities

C = TypeVar('C', bound='SupportsCapabilities')

class GeckoOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        return getattr(obj, 'get_capability')(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        return getattr(obj, 'set_capability')(self.name, value)


class AndroidStorageOption(SupportsCapabilities):
    ANDROID_STORAGE = 'androidStorage'
    android_storage = GeckoOptionsDescriptor('ANDROID_STORAGE')
    """
    Gets and Sets Current storge type
    See https://firefox-source-docs.mozilla.org/testing/geckodriver
    /Flags.html#code-android-storage-var-android-storage-var-code

    Usage
    ----
    - `self.android_storage`
    - `self.android_storage` = `value`
    """


class FirefoxOptionsOption(SupportsCapabilities):
    FIREFOX_OPTIONS = 'moz:firefoxOptions'
    firefox_options = GeckoOptionsDescriptor('ANDROID_STORAGE')
    """
    Gets and Sets Firefox mapping
    See https://developer.mozilla.org/en-US/docs/Web/WebDriver/Capabilities/firefoxOptions

    Usage
    ----
    - `self.firefox_options`
    - `self.firefox_options` = `value`
    """


class MarionettePortOption(SupportsCapabilities):
    MARIONETTE_PORT = 'marionettePort'
    marionette_port = GeckoOptionsDescriptor('MARIONETTE_PORT')
    """
    Selects the port for Geckodriver’s connection to the Marionette
    remote protocol. The existing Firefox instance must have Marionette
    enabled. To enable the remote protocol in Firefox, you can pass the
    -marionette flag. Unless the marionette.port preference has been
    user-set, Marionette will listen on port 2828, which is the default
    value for this capability.

    Usage
    ----
    - `self.marionette_port`
    - `self.marionette_port` = `value`
    """


class VerbosityOption(SupportsCapabilities):
    VERBOSITY = 'verbosity'
    verbosity = GeckoOptionsDescriptor('VERBOSITY')
    """
    Sets and Gets the  verbosity level of driver logging.
    The verbosity level of driver logging.
    By default, minimum verbosity is applied.
    Either 'debug' or 'trace'.

    Usage
    -----
    - `self.verbosity`
    - `self.verbosity` = `value`
    """