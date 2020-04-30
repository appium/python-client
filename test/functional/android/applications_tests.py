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

import os
from time import sleep

import pytest

from appium.webdriver.applicationstate import ApplicationState

from .helper.desired_capabilities import PATH
from .helper.test_helper import APIDEMO_PKG_NAME, BaseTestCase


class TestApplications(BaseTestCase):

    def test_background_app(self) -> None:
        self.driver.background_app(1)
        sleep(3)
        self.driver.launch_app()

    def test_is_app_installed(self) -> None:
        assert not self.driver.is_app_installed('sdfsdf')
        assert self.driver.is_app_installed(APIDEMO_PKG_NAME)

    @pytest.mark.skip('This causes the server to crash. no idea why')
    def test_install_app(self) -> None:
        assert not self.driver.is_app_installed('io.selendroid.testapp')
        self.driver.install_app(PATH(os.path.join('../..', 'apps', 'selendroid-test-app.apk')))
        assert self.driver.is_app_installed('io.selendroid.testapp')

    def test_remove_app(self) -> None:
        assert self.driver.is_app_installed(APIDEMO_PKG_NAME)
        self.driver.remove_app(APIDEMO_PKG_NAME)
        assert not self.driver.is_app_installed(APIDEMO_PKG_NAME)

    def test_close_and_launch_app(self) -> None:
        self.driver.close_app()
        self.driver.launch_app()
        activity = self.driver.current_activity
        assert '.ApiDemos' == activity

    def test_app_management(self) -> None:
        app_id = self.driver.current_package
        assert self.driver.query_app_state(app_id) == ApplicationState.RUNNING_IN_FOREGROUND
        self.driver.background_app(-1)
        assert self.driver.query_app_state(app_id) < ApplicationState.RUNNING_IN_FOREGROUND
        self.driver.activate_app(app_id)
        assert self.driver.query_app_state(app_id) == ApplicationState.RUNNING_IN_FOREGROUND

    def test_app_strings(self) -> None:
        strings = self.driver.app_strings()
        assert u'You can\'t wipe my data, you are a monkey!' == strings[u'monkey_wipe_data']

    def test_app_strings_with_language(self) -> None:
        strings = self.driver.app_strings('en')
        assert u'You can\'t wipe my data, you are a monkey!' == strings[u'monkey_wipe_data']

    def test_app_strings_with_language_and_file(self) -> None:
        strings = self.driver.app_strings('en', 'some_file')
        assert u'You can\'t wipe my data, you are a monkey!' == strings[u'monkey_wipe_data']

    def test_reset(self) -> None:
        self.driver.reset()
        assert self.driver.is_app_installed(APIDEMO_PKG_NAME)
