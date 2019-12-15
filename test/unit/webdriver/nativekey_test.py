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


from appium.webdriver.extensions.android.nativekey import AndroidKey


class TestAndroidKey:

    def test_has_some_codes(self):
        assert AndroidKey.ENTER == 66
        assert AndroidKey.BACK == 4
        assert AndroidKey.CAMERA == 27
        assert AndroidKey.SPACE == 62

    def test_is_gamepad_key(self):
        assert AndroidKey.is_gamepad_button(AndroidKey.BUTTON_8)
        assert not AndroidKey.is_gamepad_button(250)

    def test_is_confirm_key(self):
        assert AndroidKey.is_confirm_key(AndroidKey.SPACE)
        assert not AndroidKey.is_confirm_key(21)

    def test_is_media_key(self):
        assert AndroidKey.is_media_key(AndroidKey.MEDIA_PAUSE)
        assert not AndroidKey.is_media_key(11)

    def test_is_system_key(self):
        assert AndroidKey.is_system_key(AndroidKey.HEADSETHOOK)
        assert not AndroidKey.is_system_key(21)

    def test_is_wake_key(self):
        assert AndroidKey.is_wake_key(AndroidKey.MENU)
        assert not AndroidKey.is_wake_key(32)
