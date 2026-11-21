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

"""Start and quit one Appium session so WebDriverAgent's first, slowest launch happens before the tests.

Used by CI only. Failures are reported but don't fail the step: the tests retry on their own.
It makes a single attempt, so that it normally finishes within the step's 12-minute timeout.
"""

import sys

from appium import webdriver
from appium.webdriver.client_config import AppiumClientConfig
from test.helpers.constants import SERVER_URL_BASE

from .options import make_options


def main() -> int:
    client_config = AppiumClientConfig(remote_server_addr=SERVER_URL_BASE)
    # Match the tests' timeout: giving up earlier would leave the server still creating this
    # session, so the first test's session request would queue behind it.
    client_config.timeout = 600
    try:
        driver = webdriver.Remote(options=make_options(), client_config=client_config)
    except Exception as e:  # noqa: BLE001
        print(f'Warm-up session failed: {e}', file=sys.stderr)
        return 0
    # Give teardown its own short budget, so a session that started near the 600 s limit
    # normally still finishes within the step's 12-minute timeout, even if urllib3 retries
    # the request three times (600 s + 4 x 15 s). This is a margin, not a hard deadline:
    # the timeout applies per socket read, so a server that keeps trickling data can exceed it.
    client_config.timeout = 15
    try:
        driver.quit()
    except Exception as e:  # noqa: BLE001
        print(f'Warm-up session started but failed to quit: {e}', file=sys.stderr)
        return 0
    print('Warm-up session started and quit successfully')
    return 0


if __name__ == '__main__':
    sys.exit(main())
