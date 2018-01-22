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

from webdriver.common.screenrecord.base_screen_recording_options import BaseScreenRecordingOptions


class StopScreenRecordingOptions(BaseScreenRecordingOptions):

    def with_upload_options(self, upload_options):
        """
        The remotePath upload option is the path to the remote location,
        where the resulting video should be uploaded.
        The following protocols are supported: http/https (multipart), ftp.
        Missing value (the default setting) means the content of resulting
        file should be encoded as Base64 and passed as the endpoint response value, but
        an exception will be thrown if the generated media file is too big to
        fit into the available process memory.

        :param upload_options: see the documentation on ScreenRecordingUploadOptions
                               for more details.
        :return: self instance for chaining.
        """
        return super(StopScreenRecordingOptions, self).with_upload_options(upload_options)
