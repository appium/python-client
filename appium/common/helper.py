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


class Helper(object):

    @staticmethod
    def bytes(value, encoding):
        """
        Return a bytes-like object

        :param value: A value to convert
        :type value: string

        :param encoding: A encoding which will convert to
        :type encoding: string

        :return: string
        """

        try:
            return bytes(value, encoding)  # Python 3
        except TypeError:
            return value  # Python 2
