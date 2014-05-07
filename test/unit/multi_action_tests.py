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

from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction


class MultiActionTests(unittest.TestCase):
    def setUp(self):
        self._multi_action = MultiAction(DriverStub())

    def test_json(self):
        self.maxDiff = None
        json = {
            'actions': [
                [
                    {'action': 'press', 'options': {'x': None, 'y': None, 'element': 1}},
                    {'action': 'moveTo', 'options': {'x': 10, 'y': 20}},
                    {'action': 'release', 'options': {}}
                ],
                [
                    {'action': 'press', 'options': {'x': 11, 'y': 30, 'element': 5}},
                    {'action': 'moveTo', 'options': {'x': 12, 'y': -300}},
                    {'action': 'release', 'options': {}}
                ]
            ],
            'elementId': 0
        }
        t1 = TouchAction(DriverStub()).press(ElementStub(1)).move_to(x=10, y=20).release()
        t2 = TouchAction(DriverStub()).press(ElementStub(5), 11, 30).move_to(x=12, y=-300).release()
        self._multi_action.add(t1, t2)
        self.assertEqual(json, self._multi_action.json_wire_gestures)


class DriverStub(object):
    def execute(self, action, params):
        print "driver.execute called"


class ElementStub(object):
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id


if __name__ == "__main__":
    unittest.main()
