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

import pytest

from appium.webdriver.common.touch_action import TouchAction


class TestTouchAction(object):

    @pytest.fixture
    def touch_action(self):
        return TouchAction(DriverStub())

    def test_tap_json(self, touch_action):
        json = [
            {'action': 'tap', 'options': {'count': 1, 'element': 1}}
        ]
        touch_action.tap(ElementStub(1))
        assert json == touch_action.json_wire_gestures

    def test_tap_x_y_json(self, touch_action):
        json = [
            {'action': 'tap', 'options': {'x': 3, 'y': 4, 'count': 1, 'element': 2}}
        ]
        touch_action.tap(ElementStub(2), 3, 4)
        assert json == touch_action.json_wire_gestures

    def test_press_json(self, touch_action):
        json = [
            {'action': 'press', 'options': {'element': 3}}
        ]
        touch_action.press(ElementStub(3))
        assert json == touch_action.json_wire_gestures

    def test_press_x_y_json(self, touch_action):
        json = [
            {'action': 'press', 'options': {'element': 4, 'x': 3, 'y': 4}}
        ]
        touch_action.press(ElementStub(4), 3, 4)
        assert json == touch_action.json_wire_gestures


class DriverStub(object):
    def execute(self, _action, _params):
        print("driver.execute called")


class ElementStub(object):
    def __init__(self, e_id, _x=None, _y=None, _count=None):
        self._id = e_id

    @property
    def id(self):
        return self._id
