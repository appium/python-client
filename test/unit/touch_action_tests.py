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

import unittest

from appium.webdriver.common.touch_action import TouchAction


class TouchActionTests(unittest.TestCase):
    def setUp(self):
        self._touch_action = TouchAction(DriverStub())

    def test_tap_json(self):
        json = [
            {'action': 'tap', 'options': {'x': None, 'y': None, 'count': 1, 'element': 1}}
        ]
        self._touch_action.tap(ElementStub(1))
        self.assertEqual(json, self._touch_action.json_wire_gestures)

    def test_tap_x_y_json(self):
        json = [
            {'action': 'tap', 'options': {'x': 3, 'y': 4, 'count': 1, 'element': 2}}
        ]
        self._touch_action.tap(ElementStub(2), 3, 4)
        self.assertEqual(json, self._touch_action.json_wire_gestures)


class DriverStub(object):
    def execute(self, action, params):
        print "driver.execute called"


class ElementStub(object):
    def __init__(self, id, x=None, y=None, count=None):
        self._id = id

    @property
    def id(self):
        return self._id


if __name__ == "__main__":
    unittest.main()
