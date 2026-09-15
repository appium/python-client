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

from appium.webdriver.appium_service import _make_server_url


@pytest.mark.parametrize(
    ('args', 'expected_url'),
    [
        ([], 'http://127.0.0.1:4723/status'),
        (['--port=1234'], 'http://127.0.0.1:1234/status'),
        (['--address=appium.test'], 'http://appium.test:4723/status'),
        (['--base-path=/wd/hub'], 'http://127.0.0.1:4723/wd/hub/status'),
        (
            ['--address=appium.test', '--port=1234', '--base-path=/wd/hub'],
            'http://appium.test:1234/wd/hub/status',
        ),
        (
            ['--address', 'appium.test', '--port', '1234', '--base-path', '/wd/hub'],
            'http://appium.test:1234/wd/hub/status',
        ),
        (['-a', 'appium.test', '-p', '1234', '-pa', '/wd/hub'], 'http://appium.test:1234/wd/hub/status'),
        (['-a=appium.test', '-p=1234', '-pa=/wd/hub'], 'http://appium.test:1234/wd/hub/status'),
        (['-p', '1234', '--base-path=/wd/hub'], 'http://127.0.0.1:1234/wd/hub/status'),
        (['--base-path=/value=with=equals/'], 'http://127.0.0.1:4723/value=with=equals/status'),
        (['--port-extra=1234', '--address-extra=appium.test'], 'http://127.0.0.1:4723/status'),
    ],
)
def test_status_url_uses_cli_argument_values(args, expected_url):
    assert _make_server_url(args) == expected_url
