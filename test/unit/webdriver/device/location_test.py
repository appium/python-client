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

from test.unit.helper.test_helper import (
    appium_command,
    android_w3c_driver,
    get_httpretty_request_body
)

import httpretty

class TestWebDriverLocation(object):

    @httpretty.activate
    def test_location(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/location'),
            body='{"value": {"latitude": 11.1, "longitude": 22.2, "altitude": 33.3}}'
        )
        val = driver.location
        assert val['latitude'] == 11.1
        assert val['longitude'] == 22.2
        assert val['altitude'] == 33.3

