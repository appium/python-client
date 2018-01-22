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

import copy
from datetime import timedelta

from webdriver.common.screenrecord.base_screen_recording_options import BaseScreenRecordingOptions
from webdriver.common.screenrecord.utils import attributes_to_dict


class StartScreenRecordingOptions(BaseScreenRecordingOptions):

    def __init__(self):
        super(StartScreenRecordingOptions, self).__init__()
        self._forceRestart = None
        self._timeLimit = None

    def with_upload_options(self, upload_options):
        """
        The remotePath upload option is the path to the remote location,
        where the resulting video should be uploaded.
        The following protocols are supported: http/https (multipart), ftp.
        Missing value (the default setting) means the content of the resulting
        file should be encoded as Base64 and passed as the endpoint response value, but
        an exception will be thrown if the generated media file is too big to
        fit into the available process memory.
        This option only has an effect if there is a screen recording session in progress
        and forced restart is not enabled (the default setting).

        :param upload_options: see the documentation on ScreenRecordingUploadOptions
                               for more details.
        :return: self instance for chaining.
        """
        return super(StartScreenRecordingOptions, self).with_upload_options(upload_options)

    def with_time_limit(self, time_limit):
        """
        The maximum recording time.

        :param time_limit: The actual time limit of the recorded video. Can be either number of seconds
                           or timedelta instance.
        :return: self instance for chaining.
        """
        self._timeLimit = time_limit.total_seconds() if isinstance(time_limit, timedelta) else time_limit
        return self

    def enable_forced_restart(self):
        """
        Whether to ignore the result of previous capture and start a new recording
        immediately. By default the endpoint will try to catch and return the result of
        the previous capture if it's still available.

        :return: self instance for chaining.
        """
        self._forceRestart = True
        return self

    def build(self):
        result = super(StartScreenRecordingOptions, self).build()
        result.update(attributes_to_dict(self, ('_forceRestart', '_timeLimit')))
        return copy.copy(result)
