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

import textwrap

from test.functional.ios.helper.test_helper import BaseTestCase


class TestExecuteDriver(BaseTestCase):
    def test_batch(self) -> None:
        script = """
            const status = await driver.status();
            console.warn('warning message');
            return status;
        """

        response = self.driver.execute_driver(script=textwrap.dedent(script))
        assert(response.result['build'])
        assert(response.logs['warn'] == ['warning message'])

    def test_batch_combination_python_script(self) -> None:
        script = """
            console.warn('warning message');
            const element = await driver.findElement('accessibility id', 'Buttons');
            const rect = await driver.getElementRect(element.ELEMENT);
            return [element, rect];
        """

        response = self.driver.execute_driver(script=textwrap.dedent(script))
        r = response.result[0].rect

        assert(r == response.result[1])
