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

from webdriver.common.screenrecord.start_screen_recording_options import StartScreenRecordingOptions
from webdriver.common.screenrecord.utils import attributes_to_dict


class AndroidStartScreenRecordingOptions(StartScreenRecordingOptions):

    def __init__(self):
        super(AndroidStartScreenRecordingOptions, self).__init__()
        self._bitRate = None

    @staticmethod
    def start_screen_recording_options():
        return AndroidStartScreenRecordingOptions()

    def with_bit_rate(self, bit_rate):
        """
        The video bit rate for the video, in megabits per second.
        The default value is 4. You can increase the bit rate to improve video quality,
        but doing so results in larger movie files.

        :param bit_rate: The actual bit rate (Mb/s)
        :return: self instance for chaining.
        """
        self._bitRate = bit_rate
        return self

    def with_time_limit(self, time_limit):
        """
        The maximum recording time. The default and maximum value is 180 seconds (3 minutes).
        Setting values greater than this or less than zero will cause an exception. The minimum
        time resolution unit is one second.

        :param time_limit: The actual time limit of the recorded video. Can be a number of seconds
                           or timedelta instance.
        :return: self instance for chaining.
        """
        return super(AndroidStartScreenRecordingOptions, self).with_time_limit(time_limit)

    def build(self):
        result = super(AndroidStartScreenRecordingOptions, self).build()
        result.update(attributes_to_dict(self, ('_bitRate', )))
        return copy.copy(result)
