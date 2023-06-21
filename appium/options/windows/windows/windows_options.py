from datetime import timedelta
from typing import Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

class WindowsOptionsDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj, value):
        if self.name in ("CREATE_SESSION_TIMEOUT", "WAIT_FOR_APP_LAUNCH"):
            getattr(obj, "set_capabilities")(self.name, int(value.total_seconds() * 1000) if isinstance(value, timedelta) else value)    
        getattr(obj, "set_capabilities")(self.name, value)


class AppArgumentsOption(SupportsCapabilities):
    APP_ARGUMENTS = 'appArguments'
    app_arguments = WindowsOptionsDescriptor("APP_ARGUMENTS")


class AppTopLevelWindowOption(SupportsCapabilities):
    APP_TOP_LEVEL_WINDOW = 'appTopLevelWindow'
    app_top_level_window = WindowsOptionsDescriptor("APP_TOP_LEVEL_WINDOW")


class AppWorkingDirOption(SupportsCapabilities):
    APP_WORKING_DIR = 'appWorkingDir'
    app_working_dir = WindowsOptionsDescriptor("APP_WORKING_DIR")


class CreateSessionTimeoutOption(SupportsCapabilities):
    CREATE_SESSION_TIMEOUT = 'createSessionTimeout'
    create_session_timeout = WindowsOptionsDescriptor("CREATE_SESSION_TIMEOUT")


class ExperimentalWebDriverOption(SupportsCapabilities):
    EXPERIMENTAL_WEB_DRIVER = 'ms:experimental-webdriver'
    experimental_webdriver = WindowsOptionsDescriptor("EXPERIMENTAL_WEB_DRIVER")


class WaitForAppLaunchOption(SupportsCapabilities):
    WAIT_FOR_APP_LAUNCH = 'ms:waitForAppLaunch'
    wait_for_app_launch = WindowsOptionsDescriptor("WAIT_FOR_APP_LAUNCH")