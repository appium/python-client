Appium Python Client
====================

An extension library for adding [Selenium 3.0 draft](https://dvcs.w3.org/hg/webdriver/raw-file/tip/webdriver-spec.html) and [Mobile JSON Wire Protocol Specification draft](https://code.google.com/p/selenium/source/browse/spec-draft.md?repo=mobile)
functionality to the Python language bindings, for use with the mobile testing
framework [Appium](https://appium.io).

# Usage

The Appium Python Client is fully compliant with the Selenium 3.0 specification
draft, with some helpers to make mobile testing in Python easier. The majority of
the usage remains as it has been for Selenium 2 (WebDriver), and as the [official
Selenium Python bindings](https://pypi.python.org/pypi/selenium) begins to
implement the new specification that implementation will be used underneath, so
test code can be written that is utilizable with both bindings.

To use the new functionality now, and to use the superset of functions, instead of
including the Selenium `webdriver` module in your test code, use that from
Appium instead.

```python
from appium import webdriver
```

From there much of your test code will work with no change.

As a base for the following code examples, the following sets up the [UnitTest](https://docs.python.org/2/library/unittest.html)
environment:

```python
from appium import webdriver

desired_caps = {}
desired_caps['device'] = 'Android'
desired_caps['browserName'] = ''
desired_caps['version'] = '4.2'
desired_caps['app'] = PATH('../../../apps/selendroid-test-app.apk')
desired_caps['app-package'] = 'io.selendroid.testapp'
desired_caps['app-activity'] = '.HomeScreenActivity'

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
```

## Changed or added functionality

The methods that do change are...


### Switching between 'Native' and 'Webview'

For mobile testing the Selnium methods for switching between windows was previously
commandeered for switching between native applications and webview contexts. Methods
explicitly for this have been added to the Selenium 3 specification, so moving
forward these 'context' methods are to be used.

To get the current context, rather than calling `driver.current_window_handle` you
use

```python
current = driver.context
```

The available contexts are not retrieved using `driver.window_handles` but with

```python
driver.contexts
```

Finally, to switch to a new context, rather than `driver.switch_to.window(name)`,
use the comparable context method

```python
context_name = "WEBVIEW_1"
driver.switch_to.context(context_name)
```


### Finding elements by iOS UIAutomation search

This allows elements in iOS applications to be found using recursive element
search using the UIAutomation library. Adds the methods `driver.find_element_by_ios_uiautomation`
and `driver.find_elements_by_ios_uiautomation`.
