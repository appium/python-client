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
from typing import Optional

from typing_extensions import Self

from appium.protocols.webdriver.can_execute_commands import CanExecuteCommands
from appium.protocols.webdriver.can_execute_scripts import CanExecuteScripts
from appium.webdriver.clipboard_content_type import ClipboardContentType


class Clipboard(CanExecuteCommands, CanExecuteScripts):
    def set_clipboard(
        self, content: bytes, content_type: str = ClipboardContentType.PLAINTEXT, label: Optional[str] = None
    ) -> Self:
        """Set the content of the system clipboard

        Requires the Appium driver to support the `mobile: setClipboard` execute method.

        Args:
            content: The content to be set as bytearray string
            content_type: One of ClipboardContentType items. Only ClipboardContentType.PLAINTEXT
                is supported on Android
            label: label argument, which only works for Android

        Returns:
            Union['WebDriver', 'Clipboard']: Self instance
        """
        ext_name = 'mobile: setClipboard'
        options = {
            'content': base64.b64encode(content).decode('UTF-8'),
            'contentType': content_type,
        }
        if label:
            options['label'] = label
        self.execute_script(ext_name, options)
        return self

    def set_clipboard_text(self, text: str, label: Optional[str] = None) -> Self:
        """Copies the given text to the system clipboard

        Requires the Appium driver to support the `mobile: setClipboard` execute method.

        Args:
            text: The text to be set
            label:label argument, which only works for Android

        Returns:
            Union['WebDriver', 'Clipboard']: Self instance
        """
        return self.set_clipboard(bytes(str(text), 'UTF-8'), ClipboardContentType.PLAINTEXT, label)

    def get_clipboard(self, content_type: str = ClipboardContentType.PLAINTEXT) -> bytes:
        """Receives the content of the system clipboard

        Requires the Appium driver to support the `mobile: getClipboard` execute method.

        Args:
            content_type: One of ClipboardContentType items. Only ClipboardContentType.PLAINTEXT
                is supported on Android

        Returns:
            Clipboard content as bytearray. Or empty bytes if the clipboard is empty
        """
        ext_name = 'mobile: getClipboard'
        options = {'contentType': content_type}
        base64_str = self.execute_script(ext_name, options)
        return base64.b64decode(base64_str)

    def get_clipboard_text(self) -> str:
        """Receives the text of the system clipboard

        Requires the Appium driver to support the `mobile: getClipboard` execute method.

        Returns:
            The actual clipboard text or an empty string if the clipboard is empty
        """
        return self.get_clipboard(ClipboardContentType.PLAINTEXT).decode('UTF-8')
