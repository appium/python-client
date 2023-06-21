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


class AppOptionsDescriptor:
    def __init__(self, name) -> None:
        self.name = name

    def __get__(self, obj, cls) -> Any:
        if self.name in ("ANDROID_INSTALL_TIMEOUT", "APP_WAIT_DURATION"):
            value = getattr(obj, "get_capabilities")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj, value) -> Any:
        if self.name in ("ANDROID_INSTALL_TIMEOUT", "APP_WAIT_DURATION"):
            getattr(obj, "set_capabilities")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        getattr(obj, "set_capabilities")(self.name, value)
    

class AllowTestPackagesOption(SupportsCapabilities):
    ALLOW_TEST_PACKAGES = 'allowTestPackages'
    allow_test_packages = AppOptionsDescriptor("ALLOW_TEST_PACKAGES")


class AndroidInstallTimeoutOption(SupportsCapabilities):
    ANDROID_INSTALL_TIMEOUT = 'androidInstallTimeout'
    android_install_timeout = AppOptionsDescriptor("ANDROID_INSTALL_TIMEOUT")


class AppActivityOption(SupportsCapabilities):
    APP_ACTIVITY = 'appActivity'
    app_activity = AppOptionsDescriptor("APP_ACTIVITY")


class AppPackageOption(SupportsCapabilities):
    APP_PACKAGE = 'appPackage'
    app_package = AppOptionsDescriptor("APP_PACKAGE")


class AppWaitActivityOption(SupportsCapabilities):
    APP_WAIT_ACTIVITY = 'appWaitActivity'
    app_wait_activity = AppOptionsDescriptor("APP_WAIT_ACTIVITY")


class AppWaitDurationOption(SupportsCapabilities):
    APP_WAIT_DURATION = 'appWaitDuration'
    app_wait_duration = AppOptionsDescriptor("APP_WAIT_DURATION")


class AppWaitForLaunchOption(SupportsCapabilities):
    APP_WAIT_FOR_LAUNCH = 'appWaitForLaunch'
    app_wait_for_launch = AppOptionsDescriptor("APP_WAIT_FOR_LAUNCH")


class AppWaitPackageOption(SupportsCapabilities):
    APP_WAIT_PACKAGE = 'appWaitPackage'
    app_wait_package = AppOptionsDescriptor("APP_WAIT_PACKAGE")


class AutoGrantPermissionsOption(SupportsCapabilities):
    AUTO_GRANT_PERMISSIONS = 'autoGrantPermissions'
    auto_grant_permissions = AppOptionsDescriptor("AUTO_GRANT_PERMISSIONS")


class EnforceAppInstallOption(SupportsCapabilities):
    ENFORCE_APP_INSTALL = 'enforceAppInstall'
    enforce_app_install = AppOptionsDescriptor("ENFORCE_APP_INSTALL")


class IntentActionOption(SupportsCapabilities):
    INTENT_ACTION = 'intentAction'
    intent_action = AppOptionsDescriptor("INTENT_ACTION")


class IntentCategoryOption(SupportsCapabilities):
    INTENT_CATEGORY = 'intentCategory'
    intent_category = AppOptionsDescriptor("INTENT_CATEGORY")


class IntentFlagsOption(SupportsCapabilities):
    INTENT_FLAGS = 'intentFlags'
    intent_flags = AppOptionsDescriptor("INTENT_FLAGS")


class OptionalIntentArgumentsOption(SupportsCapabilities):
    OPTIONAL_INTENT_ARGUMENTS = 'optionalIntentArguments'
    optional_intent_arguments = AppOptionsDescriptor("OPTIONAL_INTENT_ARGUMENTS")


class RemoteAppsCacheLimitOption(SupportsCapabilities):
    REMOTE_APPS_CACHE_LIMIT = 'remoteAppsCacheLimit'
    remote_apps_cache_limit = AppOptionsDescriptor("REMOTE_APPS_CACHE_LIMIT")


class UninstallOtherPackagesOption(SupportsCapabilities):
    UNINSTALL_OTHER_PACKAGES = 'uninstallOtherPackages'
    uninstall_other_packages = AppOptionsDescriptor("UNINSTALL_OTHER_PACKAGES")