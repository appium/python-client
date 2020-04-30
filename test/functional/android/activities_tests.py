#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

from .helper.test_helper import APIDEMO_PKG_NAME, BaseTestCase


class TestActivities(BaseTestCase):
    def test_current_activity(self) -> None:
        activity = self.driver.current_activity
        assert '.ApiDemos' == activity

    def test_start_activity_this_app(self) -> None:
        self.driver.start_activity(APIDEMO_PKG_NAME, ".ApiDemos")
        self._assert_activity_contains('Demos')

        self.driver.start_activity(APIDEMO_PKG_NAME, ".accessibility.AccessibilityNodeProviderActivity")
        self._assert_activity_contains('Node')

    def test_start_activity_other_app(self) -> None:
        self.driver.start_activity(APIDEMO_PKG_NAME, ".ApiDemos")
        self._assert_activity_contains('Demos')

        self.driver.start_activity("com.android.calculator2", ".Calculator")
        self._assert_activity_contains('Calculator')

    def _assert_activity_contains(self, activity: str) -> None:
        current = self.driver.current_activity
        assert activity in current
