# Appium Python Client

[![PyPI version](https://badge.fury.io/py/Appium-Python-Client.svg)](https://badge.fury.io/py/Appium-Python-Client)
[![Downloads](https://pepy.tech/badge/appium-python-client)](https://pepy.tech/project/appium-python-client)

[![Build Status](https://dev.azure.com/AppiumCI/Appium%20CI/_apis/build/status/appium.python-client?branchName=master)](https://dev.azure.com/AppiumCI/Appium%20CI/_build/latest?definitionId=56&branchName=master)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An extension library for adding [WebDriver Protocol](https://www.w3.org/TR/webdriver/) and Appium commands to the Selenium Python language binding for use with the mobile testing framework [Appium](https://appium.io).

## Notice

Since **v1.0.0**, only Python 3.7+ is supported.

Since **v2.0.0**, the base selenium client version is v4.
The version only works in W3C WebDriver protocol format.
If you would like to use the old protocol (MJSONWP), please use v1 Appium Python client.

### Quick migration guide from v1 to v2
- Enhancement
    - Updated base Selenium Python binding version to v4
        - Removed `forceMjsonwp` since Selenium v4 and Appium Python client v2 expect only W3C WebDriver protocol
    - Methods `ActionHelpers#scroll`, `ActionHelpers#drag_and_drop`, `ActionHelpers#tap`, `ActionHelpers#swipe` and `ActionHelpers#flick` now call W3C actions as its backend
        - Please check each behavior. Their behaviors could slightly differ.
    - Added `strict_ssl` to relax SSL error such as self-signed ones
- Deprecated
    - `MultiAction` and `TouchAction` are deprecated. Please use W3C WebDriver actions.
        - e.g.
            - [appium/webdriver/extensions/action_helpers.py](appium/webdriver/extensions/action_helpers.py)
            - https://www.selenium.dev/documentation/support_packages/mouse_and_keyboard_actions_in_detail/
            - https://www.youtube.com/watch?v=oAJ7jwMNFVU
            - https://appiumpro.com/editions/30-ios-specific-touch-action-methods
            - https://appiumpro.com/editions/29-automating-complex-gestures-with-the-w3c-actions-api
    - `launch_app`, `close_app` and `reset` are deprecated. Please read [issues#15807](https://github.com/appium/appium/issues/15807) for more details

#### MultiAction/TouchAction to W3C actions

On UIA2, some elements can be handled with `touch` pointer action insead of the default `mouse` pointer action in the Selenium Python cleint.
For example, the below action builder is to replace the default one with the `touch` pointer action.

```python
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder

actions = ActionChains(driver)
# override as 'touch' pointer action
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(2)
actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
actions.w3c_actions.pointer_action.release()
actions.perform()
```

## Getting the Appium Python client

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

## Compatibility Matrix

|Appium Python Client| Selenium binding|
|----|----|
|`2.10.0`+ |`4.1.0`+ |
|`2.2.0` - `2.9.0` |`4.1.0` - `4.9.0` |
|`2.0.0` - `2.1.4` |`4.0.0` |
|`1.1.0` and below|`3.x`|

The Appium Python Client depends on [Selenium Python binding](https://pypi.org/project/selenium/), thus
the Selenium Python binding update might affect the Appium Python Client behavior.
For exampple, some changes in the Selenium binding could break the Appium client.

> **Note**
> We strongly recommend you to manage dependencies with version management tools such as Pipenv and requirements.txt
> to keep compatible version combinations.

## Usage

The Appium Python Client is fully compliant with the WebDriver Protocol
including several helpers to make mobile testing in Python easier.

To use the new functionality now, and to use the superset of functions, instead of
including the Selenium `webdriver` module in your test code, use that from
Appium instead.

```python
from appium import webdriver
```

From there much of your test code will work with no change.

As a base for the following code examples, the following sets up the [UnitTest](https://docs.python.org/3/library/unittest.html)
environment:

```python
# Python/Pytest
import pytest

from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


# HINT: fixtures below could be extracted into conftest.py
# HINT: and shared across all tests in the suite
@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of 
        # server command line arguments
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()


def create_ios_driver(custom_opts = None):    
    options = XCUITestOptions()
    options.platformVersion = '13.4'
    options.udid = '123456789ABC'
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)
    

def create_android_driver(custom_opts = None):    
    options = UiAutomator2Options()
    options.platformVersion = '10'
    options.udid = '123456789ABC'
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)


@pytest.fixture
def ios_driver_factory():
    return create_ios_driver
    

@pytest.fixture
def ios_driver():
    # prefer this fixture if there is no need to customize driver options in tests 
    driver = create_ios_driver()
    yield driver
    driver.quit()

    
@pytest.fixture
def android_driver_factory():
    return create_android_driver


@pytest.fixture
def android_driver():
    # prefer this fixture if there is no need to customize driver options in tests 
    driver = create_android_driver()
    yield driver
    driver.quit()

            
def test_ios_click(appium_service, ios_driver_factory):
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with ios_driver_factory({
        'appium:app': '/path/to/app/UICatalog.app.zip'
    }) as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='item')
        el.click()


def test_android_click(appium_service, android_driver_factory):
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with android_driver_factory({
        'appium:app': '/path/to/app/test-app.apk',
        'appium:udid': '567890',
    }) as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='item')
        el.click()
```

## Direct Connect URLs

If your Selenium/Appium server decorates the new session capabilities response with the following keys:

- `directConnectProtocol`
- `directConnectHost`
- `directConnectPort`
- `directConnectPath`

Then python client will switch its endpoint to the one specified by the values of those keys.

```python
from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.ios import XCUITestOptions

# load_capabilities API could be used to
# load options mapping stored in a dictionary
options = XCUITestOptions().load_capabilities({
    'platformVersion': '13.4',
    'deviceName': 'iPhone Simulator',
    'app': '/full/path/to/app/UICatalog.app.zip',
})

driver = webdriver.Remote(
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    'http://127.0.0.1:4723',
    options=options,
    direct_connection=True
)
```

## Relax SSL validation

`strict_ssl` option allows you to send commands to an invalid certificate host like a self-signed one.

```python
from appium import webdriver
# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.common import AppiumOptions

options = AppiumOptions()
options.platform_name = 'mac'
options.automation_name = 'safari'
# set_capability API allows to provide any custom option
# calls to it could be chained
options.set_capability('browser_name', 'safari')

# Appium1 points to http://127.0.0.1:4723/wd/hub by default
driver = webdriver.Remote('http://127.0.0.1:4723', options=options, strict_ssl=False)
```

## Set custom `AppiumConnection`

The first argument of `webdriver.Remote` can set an arbitrary command executor for you.

1. Set init arguments for the pool manager Appium Python client uses to manage http requests.

```python
from appium import webdriver
from appium.options.ios import XCUITestOptions

import urllib3
from appium.webdriver.appium_connection import AppiumConnection

# Retry connection error up to 3 times.
init_args_for_pool_manage = {
    'retries': urllib3.util.retry.Retry(total=3, connect=3, read=False)
}
appium_executor = AppiumConnection(
    remote_server_addr='http://127.0.0.1:4723',
    init_args_for_pool_manage=init_args_for_pool_manage
)

options = XCUITestOptions()
options.platformVersion = '13.4'
options.udid = '123456789ABC'
options.app = '/full/path/to/app/UICatalog.app.zip'
driver = webdriver.Remote(appium_executor, options=options)
```


2. Define a subclass of `AppiumConnection`

```python
from appium import webdriver
from appium.options.ios import XCUITestOptions

from appium.webdriver.appium_connection import AppiumConnection

class CustomAppiumConnection(AppiumConnection):
    # Can add your own methods for the custom class
    pass

custom_executor = CustomAppiumConnection(remote_server_addr='http://127.0.0.1:4723')

options = XCUITestOptions().load_capabilities({
    'platformVersion': '13.4',
    'deviceName': 'iPhone Simulator',
    'app': '/full/path/to/app/UICatalog.app.zip',
})
driver = webdriver.Remote(custom_executor, options=options)

```


## Documentation

- https://appium.github.io/python-client-sphinx/ is detailed documentation
- [functional tests](test/functional) also may help to see concrete examples.

## Development

- Code Style: [PEP-0008](https://www.python.org/dev/peps/pep-0008/)
  - Apply `black`, `isort` and `mypy` as pre commit hook
  - Run `make` command for development. See `make help` output for details
- Docstring style: [Google Style](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
- `gitchangelog` generates `CHANGELOG.rst`

### Setup

- `pip install --user pipenv`
- `python -m pipenv lock --clear`
  - If you experience `Locking Failed! unknown locale: UTF-8` error, then refer [pypa/pipenv#187](https://github.com/pypa/pipenv/issues/187) to solve it.
- `python -m pipenv install --dev --system`
- `pre-commit install`

### Run tests

You can run all of tests running on CI via `tox` in your local.

```bash
$ tox
```

You also can run particular tests like below.

#### Unit

```bash
$ pytest test/unit
```

Run with `pytest-xdist`

```bash
$ pytest -n 2 test/unit
```

#### Functional

```bash
$ pytest test/functional/ios/search_context/find_by_ios_class_chain_tests.py
```

#### In parallel for iOS

1. Create simulators named 'iPhone X - 8100' and 'iPhone X - 8101'
2. Install test libraries via pip, `pip install pytest pytest-xdist`
3. Run tests

```bash
$ pytest -n 2 test/functional/ios/search_context/find_by_ios_class_chain_tests.py
```

## Release

Follow below steps.

```bash
$ pip install twine
$ pip install git+git://github.com/vaab/gitchangelog.git # Getting via GitHub repository is necessary for Python 3.7
# Type the new version number and 'yes' if you can publish it
# You can test the command with DRY_RUN
$ DRY_RUN=1 ./release.sh
$ ./release.sh # release
```

## License

Apache License v2
