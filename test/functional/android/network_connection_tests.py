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

import pytest

from appium.webdriver.connectiontype import ConnectionType

from ..test_helper import is_ci
from .helper.test_helper import BaseTestCase


class TestNetworkConnection(BaseTestCase):
    def test_get_network_connection(self) -> None:
        nc = self.driver.network_connection
        assert isinstance(nc, int)

    @pytest.mark.skipif(condition=is_ci(), reason='Need to fix flaky test during running on CI')
    def test_set_network_connection(self) -> None:
        nc = self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        assert isinstance(nc, int)
        assert nc == ConnectionType.DATA_ONLY
