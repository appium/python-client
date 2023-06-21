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

from typing import Any

from appium.options.common.supports_capabilities import SupportsCapabilities


class GeckoOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj: Any, value: Any) -> Any:
        getattr(obj, "set_capabilities")(self.name, value)


class AndroidStorageOption(SupportsCapabilities):
    ANDROID_STORAGE = 'androidStorage'
    android_storage = GeckoOptionsDescriptor("ANDROID_STORAGE")


class FirefoxOptionsOption(SupportsCapabilities):
    FIREFOX_OPTIONS = 'moz:firefoxOptions'
    firefox_options = GeckoOptionsDescriptor("ANDROID_STORAGE")


class MarionettePortOption(SupportsCapabilities):
    MARIONETTE_PORT = 'marionettePort'
    marionette_port = GeckoOptionsDescriptor("MARIONETTE_PORT")


class VerbosityOption(SupportsCapabilities):
    VERBOSITY = 'verbosity'
    verbosity = GeckoOptionsDescriptor("VERBOSITY")