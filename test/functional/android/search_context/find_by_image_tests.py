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

import base64

import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from test.functional.android.helper import desired_capabilities
from test.functional.android.helper.test_helper import wait_for_element


class TestFindByImage(object):

    def setup_method(self) -> None:
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk.zip')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        # relax template matching
        self.driver.update_settings({"fixImageFindScreenshotDims": False,
                                     "fixImageTemplateSize": True,
                                     "autoUpdateImageElementPosition": True})

    def teardown_method(self) -> None:
        self.driver.quit()

    def test_find_based_on_image_template(self) -> None:
        image_path = desired_capabilities.PATH('file/find_by_image_success.png')
        with open(image_path, 'rb') as png_file:
            b64_data = base64.b64encode(png_file.read()).decode('UTF-8')

        el = wait_for_element(self.driver, MobileBy.IMAGE, b64_data)
        size = el.size
        assert size['width'] is not None
        assert size['height'] is not None
        loc = el.location
        assert loc['x'] is not None
        assert loc['y'] is not None
        rect = el.rect
        assert rect['width'] is not None
        assert rect['height'] is not None
        assert rect['x'] is not None
        assert rect['y'] is not None
        assert el.is_displayed()
        el.click()
        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, "Alarm")

    def test_find_multiple_elements_by_image_just_returns_one(self) -> None:
        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, "App")
        image_path = desired_capabilities.PATH('file/find_by_image_success.png')
        els = self.driver.find_elements_by_image(image_path)
        els[0].click()
        wait_for_element(self.driver, MobileBy.ACCESSIBILITY_ID, "Alarm")

    def test_find_throws_no_such_element(self) -> None:
        image_path = desired_capabilities.PATH('file/find_by_image_failure.png')
        with open(image_path, 'rb') as png_file:
            b64_data = base64.b64encode(png_file.read()).decode('UTF-8')

        with pytest.raises(TimeoutException):
            wait_for_element(self.driver, MobileBy.IMAGE, b64_data, timeout=3)

        with pytest.raises(NoSuchElementException):
            self.driver.find_element_by_image(image_path)
