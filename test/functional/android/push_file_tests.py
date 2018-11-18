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

import os
import unittest

import desired_capabilities

from appium import webdriver


class PushFileTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_push_file(self):
        test_files = ['test_image.jpg', 'test_file.txt']
        for file_name in test_files:
            source_path = os.path.dirname(os.path.abspath(__file__)) + '//' + file_name
            destination_path = '/data/local/tmp/'+file_name

            original_data = open(source_path, 'rb').read()

            self.driver.push_file(destination_path, source_path=source_path)
            new_data = self.driver.pull_file(destination_path)
            self.assertEqual(original_data, new_data)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PushFileTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
