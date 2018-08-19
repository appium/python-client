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

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import desired_capabilities

import base64


class FindByImageTests(unittest.TestCase):

    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # relax template matching
        self.driver.update_settings({"fixImageFindScreenshotDims": "false",
                                     "fixImageTemplateSize": "true",
                                     "autoUpdateImageElementPosition": "true"})

    def tearDown(self):
        self.driver.quit()

    def test_find_based_on_image_template(self):
        image_path = desired_capabilities.PATH('find_by_image_success.png')
        with open(image_path, 'rb') as png_file:
            b64_data = base64.b64encode(png_file.read()).decode('UTF-8')

        el = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.IMAGE, b64_data))
        )
        size = el.size
        self.assertIsNotNone(size['width'])
        self.assertIsNotNone(size['height'])
        loc = el.location
        self.assertIsNotNone(loc['x'])
        self.assertIsNotNone(loc['y'])
        rect = el.rect
        self.assertIsNotNone(rect['width'])
        self.assertIsNotNone(rect['height'])
        self.assertIsNotNone(rect['x'])
        self.assertIsNotNone(rect['y'])
        self.assertTrue(el.is_displayed())
        el.click()
        self.driver.find_element_by_accessibility_id("Alarm")

    def test_find_multiple_elements_by_image_just_returns_one(self):
        WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.ACCESSIBILITY_ID, "App"))
        )
        image_path = desired_capabilities.PATH('find_by_image_success.png')
        els = self.driver.find_elements_by_image(image_path)
        els[0].click()
        self.driver.find_element_by_accessibility_id("Alarm")

    def test_find_throws_no_such_element(self):
        image_path = desired_capabilities.PATH('find_by_image_failure.png')
        with open(image_path, 'rb') as png_file:
            b64_data = base64.b64encode(png_file.read()).decode('UTF-8')

        with self.assertRaises(TimeoutException):
            WebDriverWait(self.driver, 3).until(
                EC.presence_of_element_located((By.IMAGE, b64_data))
            )
        with self.assertRaises(NoSuchElementException):
            self.driver.find_element_by_image(image_path)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FindByImageTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
