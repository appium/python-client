# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from os import PathLike, fspath

from appium.options.common.supports_capabilities import SupportsCapabilities

FFMPEG_EXECUTABLE_PATH = 'ffmpegExecutablePath'


class FfmpegExecutablePathOption(SupportsCapabilities):
    @property
    def ffmpeg_executable_path(self) -> str | None:
        """
        Path to a local FFmpeg binary used for screen recording.
        """
        return self.get_capability(FFMPEG_EXECUTABLE_PATH)

    @ffmpeg_executable_path.setter
    def ffmpeg_executable_path(self, value: str | PathLike[str]) -> None:
        """
        Set the path to a local FFmpeg binary used by screen recording.
        """
        self.set_capability(FFMPEG_EXECUTABLE_PATH, fspath(value))
