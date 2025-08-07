def _get_version():
    from importlib.metadata import version
    return version("Appium-Python-Client")
version = _get_version()
