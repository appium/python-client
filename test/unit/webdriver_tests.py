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

import unittest
import requests
import httpretty

class WebDriverTests(unittest.TestCase):
    @httpretty.activate
    def test_httpbin(self):
        httpretty.register_uri(
            httpretty.POST,
            "https://httpbin.org/ip",
            body='{"origin": "127.0.0.1"}'
        )

        response = requests.post(
            'https://httpbin.org/ip',
            data = '{"username": "gabrielfalcao"}',
            headers = {
                'content-type':'text/json'
            }
        )
        self.assertEqual({"origin": "127.0.0.1"}, response.json())
        self.assertEqual(b'{"username": "gabrielfalcao"}', httpretty.last_request().body)
        self.assertEqual(1, len(httpretty.HTTPretty.latest_requests))

        response = requests.post(
            'https://httpbin.org/ip',
            data = '{"username": "gabrielfalcao"}',
            headers = {
                'content-type':'text/json'
            }
        )
        self.assertEqual(2, len(httpretty.HTTPretty.latest_requests))



if __name__ == "__main__":
    unittest.main()
