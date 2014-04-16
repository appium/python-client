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
# Android environment
import unittest
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = PATH('../../../apps/selendroid-test-app.apk')

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
```

```python
# iOS environment
import unittest
from appium import webdriver

desired_caps = {}
desired_caps['app'] = PATH('../../apps/UICatalog.app.zip')

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

```python
el = self.driver.find_element_by_ios_uiautomation('.elements()[0]')
self.assertEqual('UICatalog', el.get_attribute('name'))
```

```python
els = self.driver.find_elements_by_ios_uiautomation('elements()')
self.assertIsInstance(els, list)
```


### Finding elements by Android UIAutomator search

This allows elements in an Android application to be found using recursive element
search using the UIAutomator library. Adds the methods `driver.find_element_by_android_uiautomator`
and `driver.find_elements_by_android_uiautomator`.

```python
el = self.driver.find_element_by_android_uiautomator('new UiSelector().description("Animation")')
self.assertIsNotNone(el)
```

```python
els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
self.assertIsInstance(els, list)
```


### Finding elements by Accessibility ID

Allows for elements to be found using the "Accessibility ID". The methods take a
string representing the accessibility id or label attached to a given element, e.g., for iOS the accessibility identifier and for Android the content-description. Adds the methods
`driver.find_element_by_accessibility_id` and `find_elements_by_accessibility_id`.

```python
el = self.driver.find_element_by_accessibility_id('Animation')
self.assertIsNotNone(el)
```

```python
els = self.driver.find_elements_by_accessibility_id('Animation')
self.assertIsInstance(els, list)
```


### Touch actions

In order to accomodate mobile touch actions, and touch actions involving
multiple pointers, the Selenium 3.0 draft specifies ["touch gestures"](https://dvcs.w3.org/hg/webdriver/raw-file/tip/webdriver-spec.html#touch-gestures) and ["multi actions"](https://dvcs.w3.org/hg/webdriver/raw-file/tip/webdriver-spec.html#multiactions-1), which build upon the touch actions.

move_to: note that use keyword arguments if no element

The API is built around `TouchAction` objects, which are chains of one or more actions to be performed in a sequence. The actions are:

#### `perform`

The `perform` method sends the chain to the server in order to be enacted. It also empties the action chain, so the object can be reused. It will be at the end of all single action chains, but is unused when writing multi-action chains.

#### `tap`

The `tap` method stands alone, being unable to be chained with other methods. If you need a `tap`-like action that starts a longer chain, use `press`.

It can take either an element with an optional x-y offset, or absolute x-y coordinates for the tap, and an optional count.

```python
el = self.driver.find_element_by_accessibility_id('Animation')
action = TouchAction(self.driver)
action.tap(el).perform()
el = self.driver.find_element_by_accessibility_id('Bouncing Balls')
self.assertIsNotNone(el)
```

#### `press`

#### `long_press`

#### `release`

#### `move_to`

#### `wait`

#### `cancel`


### Multi-touch actions

In addition to chains of actions performed with in a single gesture, it is also possible to perform multiple chains at the same time, to simulate multi-finger actions. This is done through building a `MultiAction` object that comprises a number of individual `TouchAction` objects, one for each "finger".

Given two lists next to each other, we can scroll them independently but simultaneously:

```python
els = self.driver.find_elements_by_tag_name('listView')
a1 = TouchAction()
a1.press(els[0]) \
    .move_to(x=10, y=0).move_to(x=10, y=-75).move_to(x=10, y=-600).release()

a2 = TouchAction()
a2.press(els[1]) \
    .move_to(x=10, y=10).move_to(x=10, y=-300).move_to(x=10, y=-600).release()

ma = MultiAction(self.driver, els[0])
ma.add(a1, a2)
ma.perform();
```

### Appium-Specific touch actions

There are a small number of operations that mobile testers need to do quite a bit that can be relatively complicated to build using the Touch and Multi-touch Action API.  For these we provide some convenience methods in the Appium client.

#### `driver.tap`

This method, on the WedDriver object, allows for tapping with multiple fingers, simply by passing in an array of x-y coordinates to tap.

```python
el = self.driver.find_element_by_name('Touch Paint')
action.tap(el).perform()

# set up array of two coordinates
positions = []
positions.append((100, 200))
positions.append((100, 400))

self.driver.tap(positions)
```

#### `driver.swipe`

Swipe from one point to another point.

#### `driver.zoom`

Zoom in on an element, doing a pinch out operation.

#### `driver.pinch`

Zoom out on an element, doing a pinch in operation.
