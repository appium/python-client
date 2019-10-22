Appium Python Client
====================

[![PyPI version](https://badge.fury.io/py/Appium-Python-Client.svg)](https://badge.fury.io/py/Appium-Python-Client)
[![Downloads](https://pepy.tech/badge/appium-python-client)](https://pepy.tech/project/appium-python-client)

[![Build Status](https://travis-ci.org/appium/python-client.svg?branch=master)](https://travis-ci.org/appium/python-client)
[![Build Status](https://dev.azure.com/ki4070ma/python-client/_apis/build/status/appium.python-client?branchName=master)](https://dev.azure.com/ki4070ma/python-client/_build/latest?definitionId=2&branchName=master)

An extension library for adding [Selenium 3.0 draft](https://dvcs.w3.org/hg/webdriver/raw-file/tip/webdriver-spec.html) and [Mobile JSON Wire Protocol Specification draft](https://github.com/SeleniumHQ/mobile-spec/blob/master/spec-draft.md)
functionality to the Python language bindings, for use with the mobile testing
framework [Appium](https://appium.io).

# Getting the Appium Python client

There are three ways to install and use the Appium Python client.

1. Install from [PyPi](https://pypi.org), as
['Appium-Python-Client'](https://pypi.org/project/Appium-Python-Client/).

    ```shell
    pip install Appium-Python-Client
    ```

    You can see the history from [here](https://pypi.org/project/Appium-Python-Client/#history)

2. Install from source, via [PyPi](https://pypi.org). From ['Appium-Python-Client'](https://pypi.org/project/Appium-Python-Client/),
download and unarchive the source tarball (Appium-Python-Client-X.X.tar.gz).

    ```shell
    tar -xvf Appium-Python-Client-X.X.tar.gz
    cd Appium-Python-Client-X.X
    python setup.py install
    ```

3. Install from source via [GitHub](https://github.com/appium/python-client).

    ```shell
    git clone git@github.com:appium/python-client.git
    cd python-client
    python setup.py install
    ```

# Development

- Style Guide: https://www.python.org/dev/peps/pep-0008/
    - `autopep8` helps to format code automatically
        ```
        $ python -m autopep8 -r --global-config .config-pep8 -i .
        ```
    - `isort` helps to order imports automatically
        ```
        $ python -m isort -rc .
        ```
        - When you use newly 3rd party modules, add it to [.isort.cfg](.isort.cfg) to keep import order correct
- Docstring style: Google Style
    - Refer [link](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- You can customise `CHANGELOG.rst` with commit messages following [.gitchangelog.rc](.gitchangelog.rc)
    - It generates readable changelog
- Setup
    - `pip install --user pipenv`
    - `python -m pipenv lock --clear`
       - If you experience the below error, then refer [pypa/pipenv#187](https://github.com/pypa/pipenv/issues/187) to solve it.
          ```
          Locking Failed! unknown locale: UTF-8
          ```
    - `python -m pipenv install --dev --system`
    - `pre-commit install`

## Run tests

You can run all of tests running on CI via `tox` in your local.

```
$ tox
```

You also can run particular tests like below.

### Unit

```
$ py.test test/unit
```

Run with `pytest-xdist`

```
$ py.test -n 2 test/unit
```

### Functional

```
$ py.test test/functional/ios/find_by_ios_class_chain_tests.py
```

### In parallel for iOS
1. Create simulators named 'iPhone 6s - 8100' and 'iPhone 6s - 8101'
2. Install test libraries via pip
    ```
    $ pip install pytest pytest-xdist
    ```
3. Run tests
    ```
    $ py.test -n 2 test/functional/ios/find_by_ios_class_chain_tests.py
    ```

# Release

Follow below steps.

```bash
$ pip install twine
$ pip install git+git://github.com/vaab/gitchangelog.git # Getting via GitHub repository is necessary for Python 3.7
# Type the new version number and 'yes' if you can publish it
# You can test the command with DRY_RUN
$ DRY_RUN=1 ./release.sh
$ ./release.sh # release
```

# Usage

The Appium Python Client is fully compliant with the Selenium 3.0 specification
draft, with some helpers to make mobile testing in Python easier. The majority of
the usage remains as it has been for Selenium 2 (WebDriver), and as the [official
Selenium Python bindings](https://pypi.org/project/selenium/) begins to
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
desired_caps['platformVersion'] = '8.1'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = PATH('../../../apps/selendroid-test-app.apk')

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
```

```python
# iOS environment
import unittest
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '11.4'
desired_caps['automationName'] = 'xcuitest'
desired_caps['deviceName'] = 'iPhone Simulator'
desired_caps['app'] = PATH('../../apps/UICatalog.app.zip')

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
```

## Changed or added functionality

The methods that do change are...

### Direct Connect URLs

If your Selenium/Appium server decorates the new session capabilities response with the following keys:

- `directConnectProtocol`
- `directConnectHost`
- `directConnectPort`
- `directConnectPath`

Then python client will switch its endpoint to the one specified by the values of those keys.

```python
import unittest
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '11.4'
desired_caps['automationName'] = 'xcuitest'
desired_caps['deviceName'] = 'iPhone Simulator'
desired_caps['app'] = PATH('../../apps/UICatalog.app.zip')

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps, direct_connection=True)
```


### Switching between 'Native' and 'Webview'

For mobile testing the Selenium methods for switching between windows was previously
commandeered for switching between native applications and webview contexts. Methods
explicitly for this have been added to the Selenium 3 specification, so moving
forward these 'context' methods are to be used.

To get the current context, rather than calling `driver.current_window_handle` you
use

```python
current = driver.current_context
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
search using the UIAutomation library. This method is supported on iOS devices
that still support UIAutomation, that is, versions which predate XCUITEST.

Adds the methods `driver.find_element_by_ios_uiautomation`
and `driver.find_elements_by_ios_uiautomation`.

```python
el = self.driver.find_element_by_ios_uiautomation('.elements()[0]')
self.assertEqual('UICatalog', el.get_attribute('name'))
```

```python
els = self.driver.find_elements_by_ios_uiautomation('.elements()')
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

### Finding elements by Android viewtag search

This method allows finding elements using [View#tags](https://developer.android.com/reference/android/view/View#tags).
This method works with [Espresso Driver](https://github.com/appium/appium-espresso-driver).

Adds the methods `driver.find_element_by_android_viewtag` and `driver.find_elements_by_android_viewtag`.

```python
el = self.driver.find_element_by_android_viewtag('a tag name')
self.assertIsNotNone(el)
```

```python
els = self.driver.find_elements_by_android_viewtag('a tag name')
self.assertIsInstance(els, list)
```

### Finding elements by iOS predicates

This method allows finding elements using iOS predicates. The methods take a
string in the format of a predicate, including element type and the value of
fields.

Adds the methods
`driver.find_element_by_ios_predicate` and `find_elements_by_ios_predicate`.

```python
el = self.driver.find_element_by_ios_predicate('wdName == "Buttons"')
self.assertIsNotNone(el)
```

```python
els = self.driver.find_elements_by_ios_predicate('wdValue == "SearchBar" AND isWDDivisible == 1')
self.assertIsInstance(els, list)
```


### Finding elements by iOS class chain

**This method is only for [XCUITest driver](https://github.com/appium/appium-xcuitest-driver)**

This method allows finding elements using iOS class chain. The methods take
a string in the format of a class chain, including element type.

Adds the methods
`driver.find_element_by_ios_class_chain` and `find_elements_by_ios_class_chain`.

```python
el = self.driver.find_element_by_ios_class_chain('XCUIElementTypeWindow/XCUIElementTypeButton[3]')
self.assertIsNotNone(el)
```

```python
els = self.driver.find_elements_by_ios_class_chain('XCUIElementTypeWindow/XCUIElementTypeButton')
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

In order to accommodate mobile touch actions, and touch actions involving
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

In addition to chains of actions performed within a single gesture, it is also possible to perform multiple chains at the same time, to simulate multi-finger actions. This is done through building a `MultiAction` object that comprises a number of individual `TouchAction` objects, one for each "finger".

Given two lists next to each other, we can scroll them independently but simultaneously:

```python
els = self.driver.find_elements_by_class_name('listView')
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

This method, on the WebDriver object, allows for tapping with multiple fingers, simply by passing in an array of x-y coordinates to tap.

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


### Application management methods

There are times when you want, in your tests, to manage the running application,
such as installing or removing an application, etc.


#### Backgrounding an application

The method `driver.background_app` sends the running application to the background
for the specified amount of time, in seconds. After that time, the application is
brought back to the foreground.

```python
driver.background_app(1)
sleep(2)
el = driver.find_element_by_name('Animation')
assertIsNotNone(el)
```


#### Checking if an application is installed

To check if an application is currently installed on the device, use the `device.is_app_installed`
method. This method takes the bundle id of the application and return `True` or
`False`.

```python
assertFalse(self.driver.is_app_installed('sdfsdf'))
assertTrue(self.driver.is_app_installed('com.example.android.apis'))
```


#### Installing an application

To install an uninstalled application on the device, use `device.install_app`,
sending in the path to the application file or archive.

```python
assertFalse(driver.is_app_installed('io.selendroid.testapp'))
driver.install_app('/Users/isaac/code/python-client/test/apps/selendroid-test-app.apk')
assertTrue(driver.is_app_installed('io.selendroid.testapp'))
```


#### Removing an application

If you need to remove an application from the device, use `device.remove_app`,
passing in the application id.

```python
assertTrue(driver.is_app_installed('com.example.android.apis'))
driver.remove_app('com.example.android.apis')
assertFalse(driver.is_app_installed('com.example.android.apis'))
```


#### Closing and Launching an application

To launch the application specified in the desired capabilities, call `driver.launch_app`.
Closing that application is initiated by `driver.close_app`

```python
el = driver.find_element_by_name('Animation')
assertIsNotNone(el)
driver.close_app();

try:
    driver.find_element_by_name('Animation')
except Exception as e:
    pass # should not exist

driver.launch_app()
el = driver.find_element_by_name('Animation')
assertIsNotNone(el)
```

#### Resetting an application

To reset the running application, use `driver.reset`.

```python
el = driver.find_element_by_name('App')
el.click()

driver.reset()
sleep(5)

el = driver.find_element_by_name('App')
assertIsNotNone(el)
```


### Other methods


#### Start an arbitrary activity

The `driver.start_activity` method opens arbitrary activities on a device.
If the activity is not part of the application under test, it will also
launch the activity's application.

```python
driver.start_activity('com.foo.app', '.MyActivity')
```

You can also pass additional arguments to start an activity with intent as below,

```python
driver.start_activity('com.foo.app', '.MainActivity', app_wait_package='your package name')
```

and the list of additional arguments that can be passed are,

```python
             'app_wait_package'
             'app_wait_activity' 
             'intent_action' 
             'intent_category' 
             'intent_flags' 
             'optional_intent_arguments' 
             'dont_stop_app_on_reset'
```

#### Retrieving application strings

The property method `driver.app_strings` returns the application strings from
the application on the device.

```python
strings = driver.app_strings
```


#### Sending a key event to an Android device

The `driver.keyevent` method sends a keycode to the device. The keycodes can be
found in `AndroidKey` class.
Android only.

```python
from appium.webdriver.extensions.android.nativekey import AndroidKey
# sending 'Home' key event
driver.press_keycode(AndroidKey.HOME)
```


#### Hiding the keyboard in iOS

To hide the keyboard from view in iOS, use `driver.hide_keyboard`. If a key name
is sent, the keyboard key with that name will be pressed. If no arguments are
passed in, the keyboard will be hidden by tapping on the screen outside the text
field, thus removing focus from it.

```python
# get focus on text field, so keyboard comes up
el = driver.find_element_by_class_name('android.widget.TextView')
el.set_value('Testing')

el = driver.find_element_by_class_name('keyboard')
assertTrue(el.is_displayed())

driver.hide_keyboard('Done')

assertFalse(el.is_displayed())
```

```python
# get focus on text field, so keyboard comes up
el = driver.find_element_by_class_name('android.widget.TextView')
el.set_value('Testing')

el = driver.find_element_by__name('keyboard')
assertTrue(el.is_displayed())

driver.hide_keyboard()

assertFalse(el.is_displayed())
```


#### Retrieving the current running package and activity

The property method `driver.current_package` returns the name of the current
package running on the device.

```python
package = driver.current_package
assertEquals('com.example.android.apis', package)
```

The property method `driver.current_activity` returns the name of the current
activity running on the device.

```python
activity = driver.current_activity
assertEquals('.ApiDemos', activity)
```


#### Set a value directly on an element

Sometimes one needs to directly set the value of an element on the device. To do
this, the method `driver.set_value` or `element.set_value` is invoked.

```python
el = driver.find_element_by_class_name('android.widget.EditText')
driver.set_value(el, 'Testing')

text = el.get_attribute('text')
assertEqual('Testing', text)

el.set_value('More testing')
text = el.get_attribute('text')
assertEqual('More testing', text)
```


#### Retrieve a file from the device

To retrieve the contents of a file from the device, use `driver.pull_file`, which
returns the contents of the specified file encoded in [Base64](https://docs.python.org/2/library/base64.html).

```python
# pulling the strings file for our application
data = driver.pull_file('data/local/tmp/strings.json')
strings = json.loads(data.decode('base64', 'strict'))
assertEqual('You can\'t wipe my data, you are a monkey!', strings[u'monkey_wipe_data'])
```


#### Place a file on the device

To put a file onto the device at a particular place, use the `driver.push_file`
method, which takes the path and the data, encoded as [Base64](https://docs.python.org/2/library/base64.html), to be written to the file.

```python
path = 'data/local/tmp/test_push_file.txt'
data = 'This is the contents of the file to push to the device.'
driver.push_file(path, data.encode('base64'))
data_ret = driver.pull_file('data/local/tmp/test_push_file.txt').decode('base64')
self.assertEqual(data, data_ret)
```


#### End test coverage

There is functionality in the Android emulator to instrument certain activities.
For information on this, see the [Appium docs](https://github.com/appium/appium/blob/master/docs/en/android_coverage.md). To end this coverage
and retrieve the data, use `driver.end_test_coverage`, passing in the `intent`
that is being instrumentalized, and the path to the `coverage.ec` file on the
device.

```python
coverage_ec_file = driver.end_test_coverage(intent='android.intent.action.MAIN', path='')
```


#### Lock the device

To lock the device for a certain amount of time, on iOS, use `driver.lock`. The
argument is the number of seconds to wait before unlocking.


#### Shake the device

To shake the device, use `driver.shake`.


#### Appium Settings

Settings are a new concept introduced by appium. They are currently not a part of the Mobile JSON Wire Protocol, or the Webdriver spec.

Settings are a way to specify the behavior of the appium server.

Settings are:

Mutable, they can be changed during a session
Only relevant during the session they are applied. They are reset for each new session.
Control the way the appium server behaves during test automation. They do not apply to controlling the app or device under test.

See [the docs](https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/settings.md) for more information.

To get settings:
```python
settings = driver.get_settings()
```

To set settings:
```python
driver.update_settings({"some setting": "the value"})
```
