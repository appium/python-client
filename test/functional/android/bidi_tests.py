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

from typing import TYPE_CHECKING, Generator

import pytest
from selenium.webdriver.common.bidi.common import command_builder

from appium import webdriver
from appium.webdriver.client_config import AppiumClientConfig
from test.functional.test_helper import is_ci
from test.helpers.constants import SERVER_URL_BASE

from .options import make_options

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver


class AppiumLogEntry:
    """Represents a log entry from Appium BiDi."""

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


@pytest.fixture
def driver() -> Generator['WebDriver', None, None]:
    """Create and configure Chrome driver with BiDi support for testing."""
    client_config = AppiumClientConfig(remote_server_addr=SERVER_URL_BASE)
    client_config.timeout = 600
    options = make_options()
    options.web_socket_url = True
    driver = webdriver.Remote(SERVER_URL_BASE, options=options, client_config=client_config)

    yield driver

    driver.quit()


@pytest.mark.skipif(is_ci(), reason='Flaky on CI')
def test_bidi_log(driver: 'WebDriver') -> None:
    """Test BiDi logging functionality with Chrome driver."""
    log_entries = []
    bidi_log_param = {'events': ['log.entryAdded'], 'contexts': ['NATIVE_APP']}

    driver.script.conn.execute(command_builder('session.subscribe', bidi_log_param))

    def _log(entry: AppiumLogEntry):
        # e.g. {'type': 'syslog', 'level': 'info', 'source': {'realm': ''}, 'text': '08-05 13:30:32.617 29677 29709 I appium  : channel read: GET /session/d7c38859-8930-4eb0-960a-8f917c9e6a38/source', 'timestamp': 1754368241565}
        log_entries.append(entry.json)

    try:
        callback_id = driver.script.conn.add_callback(AppiumLogEntry, _log)
        driver.page_source
        assert len(log_entries) != 0
        driver.script.conn.remove_callback(AppiumLogEntry, callback_id)
    finally:
        driver.script.conn.execute(command_builder('session.unsubscribe', bidi_log_param))
