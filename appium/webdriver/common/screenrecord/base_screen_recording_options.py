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


class BaseScreenRecordingOptions(object):

    def __init__(self):
        self._upload_options = None

    def with_upload_options(self, upload_options):
        """
        Upload options for the recorded screen capture.

        :param upload_options: see the documentation on {@link ScreenRecordingUploadOptions}
                               for more details.
        :return: self instance for chaining.
        """
        self._upload_options = upload_options
        return self

    def build(self):
        """
        Builds a map, which is ready to be passed to the subordinated
        Appium API.

        :return: arguments mapping.
        """
        if self._upload_options is None:
            return {}
        return self._upload_options.build()
