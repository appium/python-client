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

from selenium.webdriver.remote.client_config import ClientConfig


class AppiumClientConfig(ClientConfig):
    def __init__(self, remote_server_addr: str, *args, **kwargs):
        self._direct_connection = kwargs.pop('direct_connection', False)
        super().__init__(remote_server_addr, *args, **kwargs)

    @property
    def direct_connection(self) -> bool:
        return self._direct_connection
