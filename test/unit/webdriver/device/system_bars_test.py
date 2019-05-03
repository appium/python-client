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


class TestWebDriverSystemBars(object):

    @httpretty.activate
    def test_get_system_bars(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/device/system_bars'),
            body=''' {"value":
                     {"statusBar":
                     {"visible": "True", "x": 0, "y": 0, "width": 1080, "height": 1920},
                     "navigationBar":
                     {"visible": "True", "x": 0, "y": 0, "width": 1080, "height": 126}}}'''
        )
        info = driver.get_system_bars()

        # FIXME Should remove eval, but it doesn't work when "True" is True in above body
        assert eval(info['statusBar']['visible']) is True
        assert info['statusBar']['x'] == 0
        assert info['statusBar']['y'] == 0
        assert info['statusBar']['width'] == 1080
        assert info['statusBar']['height'] == 1920

        assert eval(info['navigationBar']['visible']) is True
        assert info['navigationBar']['x'] == 0
        assert info['navigationBar']['y'] == 0
        assert info['navigationBar']['width'] == 1080
        assert info['navigationBar']['height'] == 126
