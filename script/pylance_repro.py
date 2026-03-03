# pyright: strict

from appium import webdriver
from appium.options.windows.windows.base import WindowsOptions

APPIUM_URL = 'http://127.0.0.1:4723'

options = WindowsOptions()

driver: webdriver.Remote = webdriver.Remote(command_executor=APPIUM_URL, options=options)
