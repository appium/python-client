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

from typing import TYPE_CHECKING, Any, TypeVar, Union

from selenium import webdriver

from ..mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from appium.webdriver.webdriver import WebDriver

T = TypeVar('T', bound=Union['WebDriver', 'ScreenRecord'])


class ScreenRecord(webdriver.Remote):

    def start_recording_screen(self: T, **options: Any) -> Union[bytes, str]:
        """Start asynchronous screen recording process.

        Keyword Args:
            remotePath (str): The remotePath upload option is the path to the remote location,
                where the resulting video from the previous screen recording should be uploaded.
                The following protocols are supported: http/https (multipart), ftp.
                Missing value (the default setting) means the content of the resulting
                file should be encoded as Base64 and passed as the endpoint response value, but
                an exception will be thrown if the generated media file is too big to
                fit into the available process memory.
                This option only has an effect if there is/was an active screen recording session
                and forced restart is not enabled (the default setting).
            user (str): The name of the user for the remote authentication.
                Only has an effect if both `remotePath` and `password` are set.
            password (str): The password for the remote authentication.
                Only has an effect if both `remotePath` and `user` are set.
            method (str): The HTTP method name ('PUT'/'POST'). PUT method is used by default.
                Only has an effect if `remotePath` is set.
            timeLimit (int): The actual time limit of the recorded video in seconds.
                The default value for both iOS and Android is 180 seconds (3 minutes).
                The maximum value for Android is 3 minutes.
                The maximum value for iOS is 10 minutes.
            forcedRestart (bool): Whether to ignore the result of previous capture and start a new recording
                immediately (`True` value). By default  (`False`) the endpoint will try to catch and
                return the result of the previous capture if it's still available.
            bugReport (str): Makes the recorder to display an additional information on the video overlay,
                such as a timestamp, that is helpful in videos captured to illustrate bugs.
                This option is only supported since API level 27 (Android P).
            videoQuality (str): [iOS only] The video encoding quality: 'low', 'medium', 'high', 'photo'. Defaults
                to 'medium'.
            videoType (str): [iOS only] The format of the screen capture to be recorded.
                Available formats: Execute `ffmpeg -codecs` in the terminal to see the list of supported video codecs.
                'mjpeg' by default. (Since Appium 1.10.0)
            videoFps (int): [iOS only] The Frames Per Second rate of the recorded video. Change this value if the
                resulting video is too slow or too fast. Defaults to 10. This can decrease the resulting file size.
            videoFilters (str): [iOS only] The FFMPEG video filters to apply. These filters allow to scale,
                flip, rotate and do many other useful transformations on the source video stream. The format of the
                property must comply with https://ffmpeg.org/ffmpeg-filters.html. (Since Appium 1.15)
            videoScale (str): [iOS only] The scaling value to apply. Read https://trac.ffmpeg.org/wiki/Scaling for
                possible values. No scale is applied by default. If videoFilters are set then the scale setting is
                effectively ignored. (Since Appium 1.10.0)
            pixelFormat (str): [iOS only] Output pixel format. Run `ffmpeg -pix_fmts` to list possible values.
                For Quicktime compatibility, set to "yuv420p" along with videoType: "libx264". (Since Appium 1.12.0)
            videoSize (str): [Android only] The video size of the generated media file. The format is WIDTHxHEIGHT.
                The default value is the device's native display resolution (if supported),
                1280x720 if not. For best results, use a size supported by your device's
                Advanced Video Coding (AVC) encoder.
            bitRate (int): [Android only] The video bit rate for the video, in megabits per second.
                The default value is 4. You can increase the bit rate to improve video quality,
                but doing so results in larger movie files.

        Returns:
            bytes: Base-64 encoded content of the recorded media
                if `stop_recording_screen` isn't called after previous `start_recording_screen`.
                Otherwise returns an empty string.
        """
        if 'password' in options:
            options['pass'] = options['password']
            del options['password']
        return self.execute(Command.START_RECORDING_SCREEN, {'options': options})['value']

    def stop_recording_screen(self: T, **options: Any) -> bytes:
        """Gather the output from the previously started screen recording to a media file.

        Keyword Args:
            remotePath (str): The remotePath upload option is the path to the remote location,
                where the resulting video should be uploaded.
                The following protocols are supported: http/https (multipart), ftp.
                Missing value (the default setting) means the content of the resulting
                file should be encoded as Base64 and passed as the endpoint response value, but
                an exception will be thrown if the generated media file is too big to
                fit into the available process memory.
            user (str): The name of the user for the remote authentication.
                Only has an effect if both `remotePath` and `password` are set.
            password (str): The password for the remote authentication.
                Only has an effect if both `remotePath` and `user` are set.
            method (str): The HTTP method name ('PUT'/'POST'). PUT method is used by default.
                Only has an effect if `remotePath` is set.

        Returns:
            bytes: Base-64 encoded content of the recorded media file or an empty string
                if the file has been successfully uploaded to a remote location
                (depends on the actual `remotePath` value).
        """
        if 'password' in options:
            options['pass'] = options['password']
            del options['password']
        return self.execute(Command.STOP_RECORDING_SCREEN, {'options': options})['value']

    # pylint: disable=protected-access
    # noinspection PyProtectedMember
    def _addCommands(self) -> None:
        self.command_executor._commands[Command.START_RECORDING_SCREEN] = \
            ('POST', '/session/$sessionId/appium/start_recording_screen')
        self.command_executor._commands[Command.STOP_RECORDING_SCREEN] = \
            ('POST', '/session/$sessionId/appium/stop_recording_screen')
