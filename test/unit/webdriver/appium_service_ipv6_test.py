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
    ('host', 'url_host'),
    [
        ('::1', '[::1]'),
        ('2001:db8::1', '[2001:db8::1]'),
        ('fe80::1%en0', '[fe80::1%en0]'),
        ('[::1]', '[::1]'),
        ('2001:db8::g', '2001:db8::g'),
        ('127.0.0.1', '127.0.0.1'),
        ('appium.test', 'appium.test'),
    ],
)
def test_status_url_formats_ip_literal_hosts(host, url_host):
    args = ['--address', host, '--port', '8123', '--base-path', '/wd/hub']
    assert _make_server_url(args) == f'http://{url_host}:8123/wd/hub/status'
