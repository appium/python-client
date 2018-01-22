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


class IOSStartScreenRecordingOptions(StartScreenRecordingOptions):

    def __init__(self):
        super(IOSStartScreenRecordingOptions, self).__init__()
        self._videoType = None
        self._videoQuality = None

    @staticmethod
    def start_screen_recording_options():
        return IOSStartScreenRecordingOptions()

    def with_video_type(self, video_type):
        """
        The format of the screen capture to be recorded.
        Available formats: "h264", "mp4" or "fmp4". Default is "mp4".
        Only works for Simulator.

        :param video_type: one of available format names.
        :return: self instance for chaining.
        """
        self._videoType = video_type
        return self

    def with_wideo_quality(self, video_quality):
        """
        The video encoding quality ('low', 'medium', 'high', 'photo' - defaults to 'medium').
        Only works for real devices.

        :param video_quality: one of possible quality preset names.
        :return: self instance for chaining.
        """
        self._videoQuality = video_quality
        return self

    def with_time_limit(self, time_limit):
        """
        The maximum recording time. The default value is 180 seconds (3 minutes).
        The maximum value is 10 minutes.
        Setting values greater than this or less than zero will cause an exception. The minimum
        time resolution unit is one second.

        :param time_limit: The actual time limit of the recorded video. Can be a number of seconds
                           or timedelta instance.
        :return: self instance for chaining.
        """
        return super(IOSStartScreenRecordingOptions, self).with_time_limit(time_limit)

    def build(self):
        result = super(IOSStartScreenRecordingOptions, self).build()
        result.update(attributes_to_dict(self, ('_videoType', '_videoQuality')))
        return copy.copy(result)
