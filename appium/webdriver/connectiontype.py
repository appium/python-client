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


"""
Connection types are specified here:
    https://code.google.com/p/selenium/source/browse/spec-draft.md?repo=mobile#120

    +--------------------+------+------+---------------+
    | Value (Alias)      | Data | Wifi | Airplane Mode |
    +====================+======+======+===============+
    | 0 (None)           | 0    | 0    | 0             |
    +--------------------+------+------+---------------+
    | 1 (Airplane Mode)  | 0    | 0    | 1             |
    +--------------------+------+------+---------------+
    | 2 (Wifi only)      | 0    | 1    | 0             |
    +--------------------+------+------+---------------+
    | 4 (Data only)      | 1    | 0    | 0             |
    +--------------------+------+------+---------------+
    | 6 (All network on) | 1    | 1    | 0             |
    +--------------------+------+------+---------------+

"""


class ConnectionType:
    NO_CONNECTION = 0
    AIRPLANE_MODE = 1
    WIFI_ONLY = 2
    DATA_ONLY = 4
    ALL_NETWORK_ON = 6
