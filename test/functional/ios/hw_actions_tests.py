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

from test.functional.ios.helper.test_helper import BaseTestCase


class TestHwActions(BaseTestCase):
    def test_lock(self) -> None:
        self.driver.lock(-1)
        try:
            assert self.driver.is_locked()
        finally:
            self.driver.unlock()
        assert not self.driver.is_locked()

    def test_shake(self) -> None:
        # TODO what can we assert about this?
        self.driver.shake()

    def test_touch_id(self) -> None:
        # nothing to assert, just verify that it doesn't blow up
        self.driver.touch_id(True)
        self.driver.touch_id(False)

    def test_toggle_touch_id_enrollment(self) -> None:
        # nothing to assert, just verify that it doesn't blow up
        self.driver.toggle_touch_id_enrollment()
