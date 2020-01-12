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

import base64
from typing import Any, Dict, Optional, TypeVar

from selenium import webdriver

from appium.webdriver.clipboard_content_type import ClipboardContentType

from ..mobilecommand import MobileCommand as Command

T = TypeVar('T', bound='Clipboard')


class Clipboard(webdriver.Remote):

    def set_clipboard(self, content: bytes, content_type: str = ClipboardContentType.PLAINTEXT,
                      label: Optional[str] = None) -> T:
        """Set the content of the system clipboard

        Args:
            content (bytes): The content to be set as bytearray string
            content_type (str): One of ClipboardContentType items. Only ClipboardContentType.PLAINTEXT
                is supported on Android
            label (:obj:`str`, optional): label argument, which only works for Android

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        options = {
            'content': base64.b64encode(content).decode('UTF-8'),
            'contentType': content_type,
        }
        if label:
            options['label'] = label
        self.execute(Command.SET_CLIPBOARD, options)
        return self

    def set_clipboard_text(self, text: str, label: Optional[str] = None) -> T:
        """Copies the given text to the system clipboard

        Args:
            text (str): The text to be set
            label (:obj:`str`, optional):label argument, which only works for Android

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """

        self.set_clipboard(bytes(str(text), 'UTF-8'), ClipboardContentType.PLAINTEXT, label)
        return self

    def get_clipboard(self, content_type: str = ClipboardContentType.PLAINTEXT) -> bytes:
        """Receives the content of the system clipboard

        Args:
            content_type (str): One of ClipboardContentType items. Only ClipboardContentType.PLAINTEXT
                is supported on Android

        Returns:
            base64-encoded string: Clipboard content. Or return an empty string if the clipboard is empty
        """
        base64_str = self.execute(Command.GET_CLIPBOARD, {
            'contentType': content_type
        })['value']
        return base64.b64decode(base64_str)

    def get_clipboard_text(self) -> str:
        """Receives the text of the system clipboard

        Return:
            str: The actual clipboard text or an empty string if the clipboard is empty
        """
        return self.get_clipboard(ClipboardContentType.PLAINTEXT).decode('UTF-8')

    # pylint: disable=protected-access

    def _addCommands(self) -> None:
        self.command_executor._commands[Command.SET_CLIPBOARD] = \
            ('POST', '/session/$sessionId/appium/device/set_clipboard')
        self.command_executor._commands[Command.GET_CLIPBOARD] = \
            ('POST', '/session/$sessionId/appium/device/get_clipboard')
