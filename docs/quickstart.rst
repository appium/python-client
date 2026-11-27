Quickstart
==========

Install the client in your Python environment:

.. code-block:: console

   $ python -m pip install Appium-Python-Client

Start an Appium server at ``127.0.0.1:4723`` with the driver for your device.
The `Appium quickstart <https://appium.io/docs/en/latest/quickstart/>`_
covers server setup and driver installation.

Android
-------

With an Android emulator running and the UiAutomator2 driver installed, open
Settings and find the Settings app's content view:

.. code-block:: python

   from appium import webdriver
   from appium.options.android import UiAutomator2Options
   from appium.webdriver.common.appiumby import AppiumBy

   options = UiAutomator2Options()
   options.app_package = 'com.android.settings'
   options.app_activity = '.Settings'

   with webdriver.Remote('http://127.0.0.1:4723', options=options) as driver:
       content = driver.find_element(AppiumBy.ID, 'android:id/content')
       assert content.is_displayed()

iOS
---

With the XCUITest driver installed, set the device name to match your booted
iOS simulator. This test opens Settings and finds its window:

.. code-block:: python

   from appium import webdriver
   from appium.options.ios import XCUITestOptions
   from appium.webdriver.common.appiumby import AppiumBy

   options = XCUITestOptions()
   options.device_name = 'iPhone 16'
   options.bundle_id = 'com.apple.Preferences'

   with webdriver.Remote('http://127.0.0.1:4723', options=options) as driver:
       window = driver.find_element(AppiumBy.CLASS_NAME, 'XCUIElementTypeWindow')
       assert window.is_displayed()
