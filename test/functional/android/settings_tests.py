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

import unittest

from .helper.test_helper import BaseTestCase


class SettingsTests(BaseTestCase):
    def test_get_settings(self) -> None:
        settings = self.driver.get_settings()
        self.assertIsNotNone(settings)

    def test_update_settings(self) -> None:
        self.driver.update_settings({"waitForIdleTimeout": 10001})
        settings = self.driver.get_settings()
        self.assertEqual(settings["waitForIdleTimeout"], 10001)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SettingsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
