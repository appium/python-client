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

import httpretty

from test.unit.helper.test_helper import android_w3c_driver, appium_command


class TestWebDriverSystemBars(object):

    @httpretty.activate
    def test_get_system_bars(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.GET,
            appium_command('/session/1234567890/appium/device/system_bars'),
            body=''' {"value":
                     {"statusBar":
                     {"visible": true, "x": 0, "y": 0, "width": 1080, "height": 1920},
                     "navigationBar":
                     {"visible": true, "x": 0, "y": 0, "width": 1080, "height": 126}}}'''
        )
        d = driver.get_system_bars()

        assert d['statusBar']['visible'] is True
        assert d['statusBar']['x'] == 0
        assert d['statusBar']['y'] == 0
        assert d['statusBar']['width'] == 1080
        assert d['statusBar']['height'] == 1920

        assert d['navigationBar']['visible'] is True
        assert d['navigationBar']['x'] == 0
        assert d['navigationBar']['y'] == 0
        assert d['navigationBar']['width'] == 1080
        assert d['navigationBar']['height'] == 126
