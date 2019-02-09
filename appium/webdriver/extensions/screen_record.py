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

from selenium import webdriver
from ..mobilecommand import MobileCommand as Command


class ScreenRecord(webdriver.Remote):

    def start_recording_screen(self, **options):
        """
        Start asynchronous screen recording process.

        :param options: The following options are supported:
        - remotePath: The remotePath upload option is the path to the remote location,
        where the resulting video from the previous screen recording should be uploaded.
        The following protocols are supported: http/https (multipart), ftp.
        Missing value (the default setting) means the content of the resulting
        file should be encoded as Base64 and passed as the endpoint response value, but
        an exception will be thrown if the generated media file is too big to
        fit into the available process memory.
        This option only has an effect if there is/was an active screen recording session
        and forced restart is not enabled (the default setting).
        - user: The name of the user for the remote authentication.
        Only has an effect if both `remotePath` and `password` are set.
        - password: The password for the remote authentication.
        Only has an effect if both `remotePath` and `user` are set.
        - method: The HTTP method name ('PUT'/'POST'). PUT method is used by default.
        Only has an effect if `remotePath` is set.
        - timeLimit: The actual time limit of the recorded video in seconds.
        The default value for both iOS and Android is 180 seconds (3 minutes).
        The maximum value for Android is 3 minutes.
        The maximum value for iOS is 10 minutes.
        - forcedRestart: Whether to ignore the result of previous capture and start a new recording
        immediately (`True` value). By default  (`False`) the endpoint will try to catch and return the result of
        the previous capture if it's still available.
        - bugReport: Makes the recorder to display an additional information on the video overlay,
        such as a timestamp, that is helpful in videos captured to illustrate bugs.
        This option is only supported since API level 27 (Android P).

        iOS Specific:
        - videoQuality: The video encoding quality: 'low', 'medium', 'high', 'photo'. Defaults to 'medium'.
        - videoType: The format of the screen capture to be recorded.
        Available formats: Execute `ffmpeg -codecs` in the terminal to see the list of supported video codecs.
        'mjpeg' by default. (Since Appium 1.10.0)
        - videoFps: The Frames Per Second rate of the recorded video. Change this value if the resulting video
        is too slow or too fast. Defaults to 10. This can decrease the resulting file size.
        - videoScale: The scaling value to apply. Read https://trac.ffmpeg.org/wiki/Scaling for possible values.
        No scale is applied by default. (Since Appium 1.10.0)

        Android Specific:
        - videoSize: The video size of the generated media file. The format is WIDTHxHEIGHT.
        The default value is the device's native display resolution (if supported),
        1280x720 if not. For best results, use a size supported by your device's
        Advanced Video Coding (AVC) encoder.
        - bitRate: The video bit rate for the video, in megabits per second.
        The default value is 4. You can increase the bit rate to improve video quality,
        but doing so results in larger movie files.

        :return: Base-64 encoded content of the recorded media file or an empty string
                 if the file has been successfully uploaded to a remote location
                 (depends on the actual `remotePath` value).
        """
        if 'password' in options:
            options['pass'] = options['password']
            del options['password']
        return self.execute(Command.START_RECORDING_SCREEN, {'options': options})['value']

    def stop_recording_screen(self, **options):
        """
        Gather the output from the previously started screen recording to a media file.

        :param options: The following options are supported:
        - remotePath: The remotePath upload option is the path to the remote location,
        where the resulting video should be uploaded.
        The following protocols are supported: http/https (multipart), ftp.
        Missing value (the default setting) means the content of the resulting
        file should be encoded as Base64 and passed as the endpoint response value, but
        an exception will be thrown if the generated media file is too big to
        fit into the available process memory.
        - user: The name of the user for the remote authentication.
        Only has an effect if both `remotePath` and `password` are set.
        - password: The password for the remote authentication.
        Only has an effect if both `remotePath` and `user` are set.
        - method: The HTTP method name ('PUT'/'POST'). PUT method is used by default.
        Only has an effect if `remotePath` is set.

        :return: Base-64 encoded content of the recorded media file or an empty string
                 if the file has been successfully uploaded to a remote location
                 (depends on the actual `remotePath` value).
        """
        if 'password' in options:
            options['pass'] = options['password']
            del options['password']
        return self.execute(Command.STOP_RECORDING_SCREEN, {'options': options})['value']

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.START_RECORDING_SCREEN] = \
            ('POST', '/session/$sessionId/appium/start_recording_screen')
        self.command_executor._commands[Command.STOP_RECORDING_SCREEN] = \
            ('POST', '/session/$sessionId/appium/stop_recording_screen')
