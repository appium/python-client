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

from appium.webdriver.applicationstate import ApplicationState
from test.functional.ios.helper.test_helper import BaseTestCase

from .helper import desired_capabilities


class TestWebDriver(BaseTestCase):

    def test_app_management(self) -> None:
        # this only works in Xcode9+
        if float(desired_capabilities.get_desired_capabilities(
                desired_capabilities.BUNDLE_ID)['platformVersion']) < 11:
            return
        assert self.driver.query_app_state(desired_capabilities.BUNDLE_ID) == ApplicationState.RUNNING_IN_FOREGROUND
        self.driver.background_app(-1)
        assert self.driver.query_app_state(desired_capabilities.BUNDLE_ID) < ApplicationState.RUNNING_IN_FOREGROUND
        self.driver.activate_app(desired_capabilities.BUNDLE_ID)
        assert self.driver.query_app_state(desired_capabilities.BUNDLE_ID) == ApplicationState.RUNNING_IN_FOREGROUND
