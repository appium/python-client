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

from appium import webdriver

from .helper.desired_capabilities import get_desired_capabilities


class TestChrome(object):
    def setup_method(self) -> None:
        caps = get_desired_capabilities()
        caps['browserName'] = 'Chrome'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)

    def teardown_method(self) -> None:
        self.driver.quit()

    def test_find_single_element(self) -> None:
        self.driver.get('http://10.0.2.2:4723/test/guinea-pig')
        self.driver.find_element_by_link_text('i am a link').click()

        assert 'I am some other page content' in self.driver.page_source
