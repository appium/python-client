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


class MobileCommand:
    # Common
    GET_SESSION = 'getSession'
    GET_ALL_SESSIONS = 'getAllSessions'

    GET_LOCATION = 'getLocation'
    SET_LOCATION = 'setLocation'

    GET_AVAILABLE_IME_ENGINES = 'getAvailableIMEEngines'
    IS_IME_ACTIVE = 'isIMEActive'
    ACTIVATE_IME_ENGINE = 'activateIMEEngine'
    DEACTIVATE_IME_ENGINE = 'deactivateIMEEngine'
    GET_ACTIVE_IME_ENGINE = 'getActiveEngine'

    CLEAR = 'clear'
    LOCATION_IN_VIEW = 'locationInView'

    CONTEXTS = 'getContexts'
    GET_CURRENT_CONTEXT = 'getCurrentContext'
    SWITCH_TO_CONTEXT = 'switchToContext'

    TOUCH_ACTION = 'touchAction'
    MULTI_ACTION = 'multiAction'

    SET_IMMEDIATE_VALUE = 'setImmediateValue'
    REPLACE_KEYS = 'replaceKeys'

    LAUNCH_APP = 'launchApp'
    CLOSE_APP = 'closeApp'
    RESET = 'reset'
    BACKGROUND = 'background'
    GET_APP_STRINGS = 'getAppStrings'

    IS_LOCKED = 'isLocked'
    LOCK = 'lock'
    UNLOCK = 'unlock'
    GET_DEVICE_TIME_GET = 'getDeviceTimeGet'
    GET_DEVICE_TIME_POST = 'getDeviceTimePost'
    INSTALL_APP = 'installApp'
    REMOVE_APP = 'removeApp'
    IS_APP_INSTALLED = 'isAppInstalled'
    TERMINATE_APP = 'terminateApp'
    ACTIVATE_APP = 'activateApp'
    QUERY_APP_STATE = 'queryAppState'
    SHAKE = 'shake'
    HIDE_KEYBOARD = 'hideKeyboard'
    PRESS_KEYCODE = 'pressKeyCode'
    LONG_PRESS_KEYCODE = 'longPressKeyCode'
    KEY_EVENT = 'keyEvent'  # Needed for Selendroid
    PUSH_FILE = 'pushFile'
    PULL_FILE = 'pullFile'
    PULL_FOLDER = 'pullFolder'
    GET_CLIPBOARD = 'getClipboard'
    SET_CLIPBOARD = 'setClipboard'
    FINGER_PRINT = 'fingerPrint'
    GET_SETTINGS = 'getSettings'
    UPDATE_SETTINGS = 'updateSettings'
    START_RECORDING_SCREEN = 'startRecordingScreen'
    STOP_RECORDING_SCREEN = 'stopRecordingScreen'
    COMPARE_IMAGES = 'compareImages'
    IS_KEYBOARD_SHOWN = 'isKeyboardShown'

    EXECUTE_DRIVER = 'executeDriver'

    GET_EVENTS = 'getLogEvents'
    LOG_EVENT = 'logCustomEvent'

    # Android
    OPEN_NOTIFICATIONS = 'openNotifications'
    START_ACTIVITY = 'startActivity'
    GET_CURRENT_ACTIVITY = 'getCurrentActivity'
    GET_CURRENT_PACKAGE = 'getCurrentPackage'
    GET_SYSTEM_BARS = 'getSystemBars'
    GET_DISPLAY_DENSITY = 'getDisplayDensity'
    TOGGLE_WIFI = 'toggleWiFi'
    TOGGLE_LOCATION_SERVICES = 'toggleLocationServices'
    END_TEST_COVERAGE = 'endTestCoverage'
    GET_PERFORMANCE_DATA_TYPES = 'getPerformanceDataTypes'
    GET_PERFORMANCE_DATA = 'getPerformanceData'
    GET_NETWORK_CONNECTION = 'getNetworkConnection'
    SET_NETWORK_CONNECTION = 'setNetworkConnection'

    # Android Emulator
    SEND_SMS = 'sendSms'
    MAKE_GSM_CALL = 'makeGsmCall'
    SET_GSM_SIGNAL = 'setGsmSignal'
    SET_GSM_VOICE = 'setGsmVoice'
    SET_NETWORK_SPEED = 'setNetworkSpeed'
    SET_POWER_CAPACITY = 'setPowerCapacity'
    SET_POWER_AC = 'setPowerAc'

    # iOS
    TOUCH_ID = 'touchId'
    TOGGLE_TOUCH_ID_ENROLLMENT = 'toggleTouchIdEnrollment'
