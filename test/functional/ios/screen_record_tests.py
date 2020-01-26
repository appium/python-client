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

from time import sleep

from test.functional.ios.helper.test_helper import BaseTestCase


class TestScreenRecord(BaseTestCase):
    def test_screen_record(self) -> None:
        self.driver.start_recording_screen()
        sleep(10)
        result = self.driver.stop_recording_screen()
        assert len(result) > 0
