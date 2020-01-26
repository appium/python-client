#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from .helper.test_helper import BaseTestCase


class TestKeyboard(BaseTestCase):
    def test_press_keycode(self) -> None:
        # TODO not sure how to test this.
        self.driver.press_keycode(176)

    def test_long_press_keycode(self) -> None:
        # TODO not sure how to test this.
        self.driver.long_press_keycode(176)
