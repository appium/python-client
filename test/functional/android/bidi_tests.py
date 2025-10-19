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

import pytest
from selenium.webdriver.common.bidi.common import command_builder

from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.client_config import AppiumClientConfig
from test.functional.test_helper import is_ci
from test.helpers.constants import SERVER_URL_BASE

from .helper.desired_capabilities import get_desired_capabilities


class AppiumLogEntry:
    event_class = 'log.entryAdded'

    def __init__(self, level, text, timestamp, source, type):
        self.level = level
        self.text = text
        self.timestamp = timestamp
        self.source = source
        self.type = type

    @property
    def json(self):
        return dict(type=self.type, level=self.level, text=self.text, timestamp=self.timestamp, source=self.source)

    @classmethod
    def from_json(cls, json: dict):
        return cls(
            level=json['level'],
            text=json['text'],
            timestamp=json['timestamp'],
            source=json['source'],
            type=json['type'],
        )


class TestChromeWithBiDi:
    """This test requires selenium python client which supports 'command_builder'"""

    def setup_method(self) -> None:
        client_config = AppiumClientConfig(remote_server_addr=SERVER_URL_BASE)
        client_config.timeout = 600
        caps = get_desired_capabilities()
        caps['webSocketUrl'] = True
        self.driver = webdriver.Remote(
            SERVER_URL_BASE, options=AppiumOptions().load_capabilities(caps), client_config=client_config
        )

    def teardown_method(self) -> None:
        self.driver.quit()

    @pytest.mark.skipif(is_ci(), reason='Flaky on CI')
    def test_bidi_log(self) -> None:
        log_entries = []
        bidi_log_param = {'events': ['log.entryAdded'], 'contexts': ['NATIVE_APP']}

        self.driver.script.conn.execute(command_builder('session.subscribe', bidi_log_param))

        def _log(entry: AppiumLogEntry):
            # e.g. {'type': 'syslog', 'level': 'info', 'source': {'realm': ''}, 'text': '08-05 13:30:32.617 29677 29709 I appium  : channel read: GET /session/d7c38859-8930-4eb0-960a-8f917c9e6a38/source', 'timestamp': 1754368241565}
            log_entries.append(entry.json)

        try:
            callback_id = self.driver.script.conn.add_callback(AppiumLogEntry, _log)
            self.driver.page_source
            assert len(log_entries) != 0
            self.driver.script.conn.remove_callback(AppiumLogEntry, callback_id)
        finally:
            self.driver.script.conn.execute(command_builder('session.unsubscribe', bidi_log_param))
