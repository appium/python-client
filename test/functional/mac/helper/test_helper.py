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
from appium.options.mac import Mac2Options
from test.helpers.constants import SERVER_URL_BASE

from .desired_capabilities import get_desired_capabilities


class BaseTestCase(object):
    def setup_method(self) -> None:
        self.driver = webdriver.Remote(SERVER_URL_BASE, options=Mac2Options().load_capabilities(get_desired_capabilities()))

    def teardown_method(self, method) -> None:  # type: ignore
        if not hasattr(self, 'driver'):
            return

        self.driver.quit()
