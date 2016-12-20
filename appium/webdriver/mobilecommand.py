#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class MobileCommand(object):
    CONTEXTS = 'getContexts',
    GET_CURRENT_CONTEXT = 'getCurrentContext',
    SWITCH_TO_CONTEXT = 'switchToContext'
    TOUCH_ACTION = 'touchAction'
    MULTI_ACTION = 'multiAction'
    OPEN_NOTIFICATIONS = 'openNotifications'
    GET_NETWORK_CONNECTION = 'getNetworkConnection'
    SET_NETWORK_CONNECTION = 'setNetworkConnection'
    GET_AVAILABLE_IME_ENGINES = 'getAvailableIMEEngines'
    IS_IME_ACTIVE = 'isIMEActive'
    ACTIVATE_IME_ENGINE = 'activateIMEEngine'
    DEACTIVATE_IME_ENGINE = 'deactivateIMEEngine'
    GET_ACTIVE_IME_ENGINE = 'getActiveEngine'
    TOGGLE_LOCATION_SERVICES = 'toggleLocationServices'
    LOCATION_IN_VIEW = 'locationInView'

    # Appium Commands
    GET_APP_STRINGS = 'getAppStrings'
    PRESS_KEYCODE = 'pressKeyCode'
    KEY_EVENT = 'keyEvent' # Needed for Selendroid
    LONG_PRESS_KEYCODE = 'longPressKeyCode'
    GET_CURRENT_ACTIVITY = 'getCurrentActivity'
    SET_IMMEDIATE_VALUE = 'setImmediateValue'
    PULL_FILE = 'pullFile'
    PULL_FOLDER = 'pullFolder'
    PUSH_FILE = 'pushFile'
    BACKGROUND = 'background'
    IS_APP_INSTALLED = 'isAppInstalled'
    INSTALL_APP = 'installApp'
    REMOVE_APP = 'removeApp'
    LAUNCH_APP = 'launchApp'
    CLOSE_APP = 'closeApp'
    END_TEST_COVERAGE = 'endTestCoverage'
    LOCK = 'lock'
    SHAKE = 'shake'
    TOUCH_ID = 'touchId'
    RESET = 'reset'
    HIDE_KEYBOARD = 'hideKeyboard'
    REPLACE_KEYS = 'replaceKeys'
    START_ACTIVITY = 'startActivity'
    GET_SETTINGS = 'getSettings'
    UPDATE_SETTINGS = 'updateSettings'
    SET_LOCATION = 'setLocation'
    GET_DEVICE_TIME = 'getDeviceTime'
    CLEAR = 'clear'