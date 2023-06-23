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
from typing import Any, TypeVar

from appium.options.common.supports_capabilities import SupportsCapabilities

C = TypeVar("C", bound="SupportsCapabilities")


class AppOptionsDescriptor:
    def __init__(self, name) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        if self.name in ("ANDROID_INSTALL_TIMEOUT", "APP_WAIT_DURATION"):
            value = getattr(obj, "get_capability")(self.name)
            return None if value is None else timedelta(milliseconds=value)
        return getattr(obj, "get_capability")(self.name)

    def __set__(self, obj: C, value: Any) -> C:
        if self.name in ("ANDROID_INSTALL_TIMEOUT", "APP_WAIT_DURATION"):
            return getattr(obj, "set_capability")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        return getattr(obj, "set_capability")(self.name, value)
    

class AllowTestPackagesOption(SupportsCapabilities):
    """
    Whether it is possible to use packages built with the test flag for
    the automated testing (literally adds -t flag to the adb install command).
    If set to true then it would be possible to use packages built with the test flag for
    the automated testing (literally adds -t flag to the adb install command). false by default.

    Usage
    -----
    - `self.allow_test_packages`
    - `self.allow_test_packages` = `value`
    """
    ALLOW_TEST_PACKAGES = 'allowTestPackages'
    allow_test_packages = AppOptionsDescriptor("ALLOW_TEST_PACKAGES")


class AndroidInstallTimeoutOption(SupportsCapabilities):
    ANDROID_INSTALL_TIMEOUT = 'androidInstallTimeout'
    android_install_timeout = AppOptionsDescriptor("ANDROID_INSTALL_TIMEOUT")
    """
    Maximum amount of time to wait until the application under test is installed.
    90000 ms by default

    Usage
    ----
    - `self.android_install_timeout`
    - `self.android_install_timeout` = `value`
    """


class AppActivityOption(SupportsCapabilities):
    APP_ACTIVITY = 'appActivity'
    app_activity = AppOptionsDescriptor("APP_ACTIVITY")
    """
    Name of the main app activity.
    Main application activity identifier. If not provided then the driver
    will try to detect it automatically from the package provided by the app capability.

    Usage
    ----
    - `self.app_activity`
    - `self.app_activity` = `value`
    """


class AppPackageOption(SupportsCapabilities):
    APP_PACKAGE = 'appPackage'
    app_package = AppOptionsDescriptor("APP_PACKAGE")
    """
    App package identifier.
    Application package identifier to be started. If not provided then the driver will
    try to detect it automatically from the package provided by the app capability.

    Usage
    -----
    - `self.app_package`
    - `self.app_package` = `value`
    """


class AppWaitActivityOption(SupportsCapabilities):
    APP_WAIT_ACTIVITY = 'appWaitActivity'
    app_wait_activity = AppOptionsDescriptor("APP_WAIT_ACTIVITY")
    """
    Name of the app activity to wait for.
    Identifier of the activity that the driver should wait for
    (not necessarily the main one).
    If not provided then defaults to appium:appActivity.

    Usage
    ----
    - `self.app_wait_activity`
    - `self.app_wait_activity` = `value`
    """


class AppWaitDurationOption(SupportsCapabilities):
    APP_WAIT_DURATION = 'appWaitDuration'
    app_wait_duration = AppOptionsDescriptor("APP_WAIT_DURATION")
    """
    Identifier of the app package to wait for.
    Maximum amount of time to wait until the application under test is started
    (e.g. an activity returns the control to the caller). 20000 ms by default.

    Usage
    -----
    - `self.app_wait_duration`
    - `self.app_wait_duration` = `value`
    """


class AppWaitForLaunchOption(SupportsCapabilities):
    APP_WAIT_FOR_LAUNCH = 'appWaitForLaunch'
    app_wait_for_launch = AppOptionsDescriptor("APP_WAIT_FOR_LAUNCH")
    """
    Whether to block until the app under test returns the control to the
    caller after its activity has been started by Activity Manager.
    (true, the default value) or to continue the test without waiting for that (false).

    Usage
    ----
    - `self.app_wait_for_launch`
    - `self.app_wait_for_launch` = `value`
    """


class AppWaitPackageOption(SupportsCapabilities):
    APP_WAIT_PACKAGE = 'appWaitPackage'
    app_wait_package = AppOptionsDescriptor("APP_WAIT_PACKAGE")
    """
    Identifier of the app package to wait for.
    (not necessarily the main one).
    If not provided then defaults to appium:appPackage.

    Usage
    -----
    - `self.app_wait_package`
    - `self.app_wait_package` = `value`
    """


class AutoGrantPermissionsOption(SupportsCapabilities):
    AUTO_GRANT_PERMISSIONS = 'autoGrantPermissions'
    auto_grant_permissions = AppOptionsDescriptor("AUTO_GRANT_PERMISSIONS")
    """
    Whether to grant all the requested application permissions
    automatically when a test starts.
    `False` by default.

    Usage
    -----
    - `self.auto_grant_permissions`
    - `self.auto_grant_permissions` = `value`
    """


class EnforceAppInstallOption(SupportsCapabilities):
    ENFORCE_APP_INSTALL = 'enforceAppInstall'
    enforce_app_install = AppOptionsDescriptor("ENFORCE_APP_INSTALL")
    """
    Whether the application under test is always reinstalled even
    if a newer version of it already exists on the device under test.
    `False` by default.

    Usage
    -----
    - `self.enforce_app_install`
    - `self.enforce_app_install` = `value`
    """


class IntentActionOption(SupportsCapabilities):
    INTENT_ACTION = 'intentAction'
    intent_action = AppOptionsDescriptor("INTENT_ACTION")
    """
    Intent action to be applied when
    starting the given appActivity by Activity Manager.
    Set an optional intent action to be applied when
    starting the given appActivity by Activity Manager.

    Usage
    -----
    - `self.intent_action`
    - `self.intent_action` = `value`
    """


class IntentCategoryOption(SupportsCapabilities):
    INTENT_CATEGORY = 'intentCategory'
    intent_category = AppOptionsDescriptor("INTENT_CATEGORY")
    """
    Gets and Sets an optional intent category to be applied when
    starting the given appActivity by Activity Manager.

    Usage
    -----
    - `self.intent_category`
    - `self.intent_category` = `value`
    """


class IntentFlagsOption(SupportsCapabilities):
    INTENT_FLAGS = 'intentFlags'
    intent_flags = AppOptionsDescriptor("INTENT_FLAGS")
    """
    Gets and Sets optional intent flags to be applied when
    starting the given appActivity by Activity Manager.

    Usage
    -----
    - `self.intent_flags`
    - `self.intent_flags` = `value`
    """


class OptionalIntentArgumentsOption(SupportsCapabilities):
    OPTIONAL_INTENT_ARGUMENTS = 'optionalIntentArguments'
    optional_intent_arguments = AppOptionsDescriptor("OPTIONAL_INTENT_ARGUMENTS")
    """
    Gets and Sets optional intent arguments to be applied when
    starting the given appActivity by Activity Manager.

    Usage
    -----
    - `self.optional_intent_arguments`
    - `self.optional_intent_arguments` = `value`
    """


class RemoteAppsCacheLimitOption(SupportsCapabilities):
    REMOTE_APPS_CACHE_LIMIT = 'remoteAppsCacheLimit'
    remote_apps_cache_limit = AppOptionsDescriptor("REMOTE_APPS_CACHE_LIMIT")
    """
    Gets and Sets the maximum amount of application packages to be cached on the device under test.
    This is needed for devices that don't support streamed installs (Android 7 and below),
    because ADB must push app packages to the device first in order to install them,
    which takes some time. Setting this capability to zero disables apps caching.
    10 by default.

    Usage
    -----
    - `self.remote_apps_cache_limit`
    - `self.remote_apps_cache_limit` = `value`
    """


class UninstallOtherPackagesOption(SupportsCapabilities):
    UNINSTALL_OTHER_PACKAGES = 'uninstallOtherPackages'
    uninstall_other_packages = AppOptionsDescriptor("UNINSTALL_OTHER_PACKAGES")
    """
    Allows to Get and Set one or more comma-separated package
    identifiers to be uninstalled from the device before a test starts.

    Usage
    -----
    - `self.uninstall_other_packages`
    - `self.uninstall_other_packages` = `value`
    """