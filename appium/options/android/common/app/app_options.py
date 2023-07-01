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

from appium.options.base_options import OptionsDescriptor
from appium.options.transformers import DurationTransformer
from appium.options.common.supports_capabilities import SupportsCapabilities


class AllowTestPackagesOption(SupportsCapabilities):
    ALLOW_TEST_PACKAGES = 'allowTestPackages'
    allow_test_packages = OptionsDescriptor('ALLOW_TEST_PACKAGES')
    """
    Whether it is possible to use packages built with the test flag for
    the automated testing (literally adds -t flag to the adb install command).
    If set to true then it would be possible to use packages built with the test flag for
    the automated testing (literally adds -t flag to the adb install command). false by default.

    Usage
    -----
    - Get
        - `self.allow_test_packages`
    - Set
        - `self.allow_test_packages` = `value`

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


class AndroidInstallTimeoutOption(SupportsCapabilities):
    ANDROID_INSTALL_TIMEOUT = 'androidInstallTimeout'

    _transform_duration_get = DurationTransformer.transform_duration_get
    _transform_duration_set = DurationTransformer.transform_duration_set
    android_install_timeout = OptionsDescriptor('ANDROID_INSTALL_TIMEOUT', _transform_duration_get, _transform_duration_set)
    """
    Maximum amount of time to wait until the application under test is installed.
    90000 ms by default

    Usage
    ----
    - Get
        - `self.android_install_timeout`
    - Set
        - `self.android_install_timeout` = `value`

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


class AppActivityOption(SupportsCapabilities):
    APP_ACTIVITY = 'appActivity'
    app_activity = OptionsDescriptor('APP_ACTIVITY')
    """
    Name of the main app activity.
    Main application activity identifier. If not provided then the driver
    will try to detect it automatically from the package provided by the app capability.

    Usage
    ----
    - Get
        - `self.app_activity`
    - Set
        - `self.app_activity` = `value`

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


class AppPackageOption(SupportsCapabilities):
    APP_PACKAGE = 'appPackage'
    app_package = OptionsDescriptor('APP_PACKAGE')
    """
    App package identifier.
    Application package identifier to be started. If not provided then the driver will
    try to detect it automatically from the package provided by the app capability.

    Usage
    -----
    - Get
        - `self.app_package`
    - Set
        - `self.app_package` = `value`

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


class AppWaitActivityOption(SupportsCapabilities):
    APP_WAIT_ACTIVITY = 'appWaitActivity'
    app_wait_activity = OptionsDescriptor('APP_WAIT_ACTIVITY')
    """
    Name of the app activity to wait for.
    Identifier of the activity that the driver should wait for
    (not necessarily the main one).
    If not provided then defaults to appium:appActivity.

    Usage
    ----
    - Get
        - `self.app_wait_activity`
    - Set
        - `self.app_wait_activity` = `value`

    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - None
    """


class AppWaitDurationOption(SupportsCapabilities):
    APP_WAIT_DURATION = 'appWaitDuration'
    app_wait_duration = OptionsDescriptor('APP_WAIT_DURATION')
    """
    Identifier of the app package to wait for.
    Maximum amount of time to wait until the application under test is started
    (e.g. an activity returns the control to the caller). 20000 ms by default.

    Usage
    -----
    - Get
        - `self.app_wait_duration`
    - Set
        - `self.app_wait_duration` = `value`

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


class AppWaitForLaunchOption(SupportsCapabilities):
    APP_WAIT_FOR_LAUNCH = 'appWaitForLaunch'
    app_wait_for_launch = OptionsDescriptor('APP_WAIT_FOR_LAUNCH')
    """
    Whether to block until the app under test returns the control to the
    caller after its activity has been started by Activity Manager.
    (true, the default value) or to continue the test without waiting for that (false).

    Usage
    ----
    - Get
        - `self.app_wait_for_launch`
    - Set
        - `self.app_wait_for_launch` = `value`

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


class AppWaitPackageOption(SupportsCapabilities):
    APP_WAIT_PACKAGE = 'appWaitPackage'
    app_wait_package = OptionsDescriptor('APP_WAIT_PACKAGE')
    """
    Identifier of the app package to wait for.
    (not necessarily the main one).
    If not provided then defaults to appium:appPackage.

    Usage
    -----
    - Get
        - `self.app_wait_package`
    - Set
        - `self.app_wait_package` = `value`

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


class AutoGrantPermissionsOption(SupportsCapabilities):
    AUTO_GRANT_PERMISSIONS = 'autoGrantPermissions'
    auto_grant_permissions = OptionsDescriptor('AUTO_GRANT_PERMISSIONS')
    """
    Whether to grant all the requested application permissions
    automatically when a test starts.
    `False` by default.

    Usage
    -----
    - Get
        - `self.auto_grant_permissions`
    - Set
        - `self.auto_grant_permissions` = `value`

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


class EnforceAppInstallOption(SupportsCapabilities):
    ENFORCE_APP_INSTALL = 'enforceAppInstall'
    enforce_app_install = OptionsDescriptor('ENFORCE_APP_INSTALL')
    """
    Whether the application under test is always reinstalled even
    if a newer version of it already exists on the device under test.
    `False` by default.

    Usage
    -----
    - Get
        - `self.enforce_app_install`
    - Set
        - `self.enforce_app_install` = `value`

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


class IntentActionOption(SupportsCapabilities):
    INTENT_ACTION = 'intentAction'
    intent_action = OptionsDescriptor('INTENT_ACTION')
    """
    Intent action to be applied when
    starting the given appActivity by Activity Manager.
    Set an optional intent action to be applied when
    starting the given appActivity by Activity Manager.

    Usage
    -----
    - Get
        - `self.intent_action`
    - Set
        - `self.intent_action` = `value`

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


class IntentCategoryOption(SupportsCapabilities):
    INTENT_CATEGORY = 'intentCategory'
    intent_category = OptionsDescriptor('INTENT_CATEGORY')
    """
    Gets and Sets an optional intent category to be applied when
    starting the given appActivity by Activity Manager.

    Usage
    -----
    - Get
        - `self.intent_category`
    - Set
        - `self.intent_category` = `value`

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


class IntentFlagsOption(SupportsCapabilities):
    INTENT_FLAGS = 'intentFlags'
    intent_flags = OptionsDescriptor('INTENT_FLAGS')
    """
    Gets and Sets optional intent flags to be applied when
    starting the given appActivity by Activity Manager.

    Usage
    -----
    - Get
        - `self.intent_flags`
    - Set
        - `self.intent_flags` = `value`

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


class OptionalIntentArgumentsOption(SupportsCapabilities):
    OPTIONAL_INTENT_ARGUMENTS = 'optionalIntentArguments'
    optional_intent_arguments = OptionsDescriptor('OPTIONAL_INTENT_ARGUMENTS')
    """
    Gets and Sets optional intent arguments to be applied when
    starting the given appActivity by Activity Manager.

    Usage
    -----
    - Get
        - `self.optional_intent_arguments`
    - Set
        - `self.optional_intent_arguments` = `value`

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


class RemoteAppsCacheLimitOption(SupportsCapabilities):
    REMOTE_APPS_CACHE_LIMIT = 'remoteAppsCacheLimit'
    remote_apps_cache_limit = OptionsDescriptor('REMOTE_APPS_CACHE_LIMIT')
    """
    Gets and Sets the maximum amount of application packages to be cached on the device under test.
    This is needed for devices that don't support streamed installs (Android 7 and below),
    because ADB must push app packages to the device first in order to install them,
    which takes some time. Setting this capability to zero disables apps caching.
    10 by default.

    Usage
    -----
    - Get
        - `self.remote_apps_cache_limit`
    - Set
        - `self.remote_apps_cache_limit` = `value`

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


class UninstallOtherPackagesOption(SupportsCapabilities):
    UNINSTALL_OTHER_PACKAGES = 'uninstallOtherPackages'
    uninstall_other_packages = OptionsDescriptor('UNINSTALL_OTHER_PACKAGES')
    """
    Allows to Get and Set one or more comma-separated package
    identifiers to be uninstalled from the device before a test starts.

    Usage
    -----
    - Get
        - `self.uninstall_other_packages`
    - Set
        - `self.uninstall_other_packages` = `value`

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