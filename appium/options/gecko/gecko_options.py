from typing import Optional

from appium.options.common.supports_capabilities import SupportsCapabilities


class GeckoOptionsDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, cls):
        return getattr(obj, "get_capabilities")(self.name)

    def __set__(self, obj, value):
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