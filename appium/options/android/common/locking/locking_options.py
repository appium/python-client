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

from datetime import timedelta
from typing import Any

from appium.options.common.supports_capabilities import SupportsCapabilities


class SkipLockOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: Any, cls: Any) -> Any:
        if self.name == "UNLOCK_SUCCESS_TIMEOUT":
            value = getattr(obj, "get_capabilities")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj: Any, value: Any) -> Any:
        if self.name == "UNLOCK_SUCCESS_TIMEOUT":
            getattr(obj, "set_capabilities")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)
        getattr(obj, "set_capabilities")(self.name, value)


class SkipUnlockOption(SupportsCapabilities):
    SKIP_UNLOCK = 'skipUnlock'
    skip_unlock = SkipLockOptionsDescriptor("SKIP_UNLOCK")


class UnlockKeyOption(SupportsCapabilities):
    UNLOCK_KEY = 'unlockKey'
    unlock_key = SkipLockOptionsDescriptor("UNLOCK_KEY")

class UnlockStrategyOption(SupportsCapabilities):
    UNLOCK_STRATEGY = 'unlockStrategy'
    unlock_strategy = SkipLockOptionsDescriptor("UNLOCK_STRATEGY")


class UnlockSuccessTimeoutOption(SupportsCapabilities):
    UNLOCK_SUCCESS_TIMEOUT = 'unlockSuccessTimeout'
    unlock_success_timeout = SkipLockOptionsDescriptor("UNLOCK_SUCCESS_TIMEOUT")


class UnlockTypeOption(SupportsCapabilities):
    UNLOCK_TYPE = 'unlockType'
    unlock_type = SkipLockOptionsDescriptor("UNLOCK_TYPE")