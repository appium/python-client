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

from typing import Any, Union

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands

from ..mobilecommand import MobileCommand as Command


class ScreenRecord(CanExecuteCommands):
    def start_recording_screen(self, **options: Any) -> Union[bytes, str]:
        """Start asynchronous screen recording process.

        +--------------+-----+---------+-----+-------+
        | Keyword Args | iOS | Android | Win | macOS |
        +==============+=====+=========+=====+=======+
        | remotePath   | O   | O       | O   | O     |
        +--------------+-----+---------+-----+-------+
        | user         | O   | O       | O   | O     |
        +--------------+-----+---------+-----+-------+
        | password     | O   | O       | O   | O     |
        +--------------+-----+---------+-----+-------+
        | method       | O   | O       | O   | O     |
        +--------------+-----+---------+-----+-------+
        | timeLimit    | O   | O       | O   | O     |
        +--------------+-----+---------+-----+-------+
        | forceRestart | O   | O       | O   | O     |
        +--------------+-----+---------+-----+-------+
        | fileFieldName| O   | O       | O   | O     |
        +--------------+-----+---------+-----+-------+
        | formFields   | O   | O       | O   | O     |
        +--------------+-----+---------+-----+-------+
        | headers      | O   | O       | O   | O     |
        +--------------+-----+---------+-----+-------+
        | videoQuality | O   |         |     |       |
        +--------------+-----+---------+-----+-------+
        | videoType    | O   |         |     |       |
        +--------------+-----+---------+-----+-------+
        | videoFps     | O   |         |     |       |
        +--------------+-----+---------+-----+-------+
        | videoFilter  | O   |         | O   | O     |
        +--------------+-----+---------+-----+-------+
        | videoScale   | O   |         |     |       |
        +--------------+-----+---------+-----+-------+
        | pixelFormat  | O   |         |     |       |
        +--------------+-----+---------+-----+-------+
        | videoSize    |     | O       |     |       |
        +--------------+-----+---------+-----+-------+
        | bitRate      |     | O       |     |       |
        +--------------+-----+---------+-----+-------+
        | bugReport    |     | O       |     |       |
        +--------------+-----+---------+-----+-------+
        | fps          |     |         | O   | O     |
        +--------------+-----+---------+-----+-------+
        | captureCursor|     |         | O   | O     |
        +--------------+-----+---------+-----+-------+
        | captureClicks|     |         | O   | O     |
        +--------------+-----+---------+-----+-------+
        | deviceId     |     |         |     | O     |
        +--------------+-----+---------+-----+-------+
        | preset       |     |         | O   | O     |
        +--------------+-----+---------+-----+-------+
        | audioInput   |     |         | O   |       |
        +--------------+-----+---------+-----+-------+

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
                The default value for macOS is 600 seconds (10 minutes).
                The maximum value for Android is 3 minutes.
                The maximum value for iOS is 10 minutes.
                The maximum value for macOS is 10000 seconds (166 minutes).
            forcedRestart (bool): Whether to ignore the result of previous capture and start a new recording
                immediately (`True` value). By default  (`False`) the endpoint will try to catch and
                return the result of the previous capture if it's still available.
            fileFieldName (str): [multipart/form-data requests] The name of the form field
                containing the binary payload. "file" by default. (Since Appium 1.18.0)
            formFields (dict): [multipart/form-data requests] Additional form fields mapping. If any entry has
                the same key as `fileFieldName` then it is going to be ignored. (Since Appium 1.18.0)
            headers (dict): [multipart/form-data requests] Headers mapping (Since Appium 1.18.0)

            videoQuality (str): [iOS] The video encoding quality: 'low', 'medium', 'high', 'photo'. Defaults
                to 'medium'.
            videoType (str): [iOS] The format of the screen capture to be recorded.
                Available formats: Execute `ffmpeg -codecs` in the terminal to see the list of supported video codecs.
                'mjpeg' by default. (Since Appium 1.10.0)
            videoFps (int): [iOS] The Frames Per Second rate of the recorded video. Change this value if the
                resulting video is too slow or too fast. Defaults to 10. This can decrease the resulting file size.
            videoFilters (str): [iOS, Win, macOS] The FFMPEG video filters to apply. These filters allow to scale,
                flip, rotate and do many other useful transformations on the source video stream. The format of the
                property must comply with https://ffmpeg.org/ffmpeg-filters.html. (Since Appium 1.15)
            videoScale (str): [iOS] The scaling value to apply. Read https://trac.ffmpeg.org/wiki/Scaling for
                possible values. No scale is applied by default. If videoFilters are set then the scale setting is
                effectively ignored. (Since Appium 1.10.0)
            pixelFormat (str): [iOS] Output pixel format. Run `ffmpeg -pix_fmts` to list possible values.
                For Quicktime compatibility, set to "yuv420p" along with videoType: "libx264". (Since Appium 1.12.0)

            videoSize (str): [Android] The video size of the generated media file. The format is WIDTHxHEIGHT.
                The default value is the device's native display resolution (if supported),
                1280x720 if not. For best results, use a size supported by your device's
                Advanced Video Coding (AVC) encoder.
            bitRate (int): [Android] The video bit rate for the video, in megabits per second.
                The default value is 4. You can increase the bit rate to improve video quality,
                but doing so results in larger movie files.
            bugReport (str): [Android] Makes the recorder to display an additional information on the video overlay,
                such as a timestamp, that is helpful in videos captured to illustrate bugs.
                This option is only supported since API level 27 (Android P).

            fps (int): [Win, macOS] The count of frames per second in the resulting video.
                Increasing fps value also increases the size of the resulting video file and the CPU usage.
            captureCursor (bool): [Win, macOS] Whether to capture the mouse cursor while recording the screen.
                Disabled by default.
            captureClick (bool): [Win, macOS] Whether to capture the click gestures while recording the screen.
                Disabled by default.
            deviceId (int): [macOS] Screen device index to use for the recording.
                The list of available devices could be retrieved using
                `ffmpeg -f avfoundation -list_devices true -i` command.
                This option is mandatory and must be always provided.
            preset (str): [Win, macOS] A preset is a collection of options that will provide a certain encoding
                speed to compression ratio. A slower preset will provide better compression
                (compression is quality per filesize). This means that, for example, if you target a certain file size
                or constant bit rate, you will achieve better quality with a slower preset.
                Read https://trac.ffmpeg.org/wiki/Encode/H.264 for more details.
                Possible values are 'ultrafast', 'superfast', 'veryfast'(default), 'faster', 'fast', 'medium', 'slow',
                'slower', 'veryslow'

        Returns:
            bytes: Base-64 encoded content of the recorded media
                if `stop_recording_screen` isn't called after previous `start_recording_screen`.
                Otherwise returns an empty string.
        """
        if 'password' in options:
            options['pass'] = options['password']
            del options['password']
        return self.execute(Command.START_RECORDING_SCREEN, {'options': options})['value']

    def stop_recording_screen(self, **options: Any) -> bytes:
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
            fileFieldName (str): [multipart/form-data requests] The name of the form field
                containing the binary payload. "file" by default. (Since Appium 1.18.0)
            formFields (dict): [multipart/form-data requests] Additional form fields mapping. If any entry has
                the same key as `fileFieldName` then it is going to be ignored. (Since Appium 1.18.0)
            headers (dict): [multipart/form-data requests] Headers mapping (Since Appium 1.18.0)

        Returns:
            bytes: Base-64 encoded content of the recorded media file or an empty string
                if the file has been successfully uploaded to a remote location
                (depends on the actual `remotePath` value).
        """
        if 'password' in options:
            options['pass'] = options['password']
            del options['password']
        return self.execute(Command.STOP_RECORDING_SCREEN, {'options': options})['value']

    def _add_commands(self) -> None:
        self.command_executor.add_command(
            Command.START_RECORDING_SCREEN,
            'POST',
            '/session/$sessionId/appium/start_recording_screen',
        )
        self.command_executor.add_command(
            Command.STOP_RECORDING_SCREEN,
            'POST',
            '/session/$sessionId/appium/stop_recording_screen',
        )
