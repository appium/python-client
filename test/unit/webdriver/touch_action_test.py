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
            {'action': 'tap', 'options': {'x': 3, 'y': 4, 'count': 1, 'element': 1}}
        ]
        touch_action.tap(ElementStub(1), 3, 4)
        assert json == touch_action.json_wire_gestures

    def test_press_json(self, touch_action):
        json = [
            {'action': 'press', 'options': {'element': 1}}
        ]
        touch_action.press(ElementStub(1))
        assert json == touch_action.json_wire_gestures

    def test_press_pressure_json(self, touch_action):
        json = [
            {'action': 'press', 'options': {'element': 1, 'pressure': 1.0}}
        ]
        touch_action.press(ElementStub(1), pressure=1.0)
        assert json == touch_action.json_wire_gestures

    def test_press_x_y_json(self, touch_action):
        json = [
            {'action': 'press', 'options': {'element': 1, 'x': 3, 'y': 4}}
        ]
        touch_action.press(ElementStub(1), 3, 4)
        assert json == touch_action.json_wire_gestures

    def test_long_press_json(self, touch_action):
        json = [
            {'action': 'longPress', 'options': {'element': 1, 'duration': 2000}}
        ]
        touch_action.long_press(ElementStub(1), duration=2000)
        assert json == touch_action.json_wire_gestures

    def test_long_press_x_y_json(self, touch_action):
        json = [
            {'action': 'longPress', 'options': {'element': 1, 'x': 3, 'y': 4, 'duration': 1000}}
        ]
        touch_action.long_press(ElementStub(1), 3, 4)
        assert json == touch_action.json_wire_gestures

    def test_wait_json(self, touch_action):
        json = [
            {'action': 'wait', 'options': {'ms': 10}}
        ]
        touch_action.wait(10)
        assert json == touch_action.json_wire_gestures

    def test_wait_without_ms_json(self, touch_action):
        json = [
            {'action': 'wait', 'options': {'ms': 0}}
        ]
        touch_action.wait()
        assert json == touch_action.json_wire_gestures

    def test_move_to_json(self, touch_action):
        json = [
            {'action': 'moveTo', 'options': {'element': 1, 'x': 3, 'y': 4}}
        ]
        touch_action.move_to(ElementStub(1), 3, 4)
        assert json == touch_action.json_wire_gestures

    def test_release_json(self, touch_action):
        json = [
            {'action': 'release', 'options': {}}
        ]
        touch_action.release()
        assert json == touch_action.json_wire_gestures

    def test_perform_json(self, touch_action):
        json_tap = [
            {'action': 'tap', 'options': {'element': 1, 'count': 1}}
        ]
        touch_action.tap(ElementStub(1))
        assert json_tap == touch_action.json_wire_gestures
        touch_action.perform()
        assert [] == touch_action.json_wire_gestures


class DriverStub(object):
    def execute(self, _action, _params):
        print("driver.execute called")


class ElementStub(object):
    def __init__(self, e_id, _x=None, _y=None, _count=None):
        self._id = e_id

    @property
    def id(self):
        return self._id
