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

import os
from typing import Any, Dict, Optional, Tuple, Union

from appium.common.helper import encode_file_to_base64
from appium.webdriver.extensions.flutter_integration.flutter_finder import FlutterFinder
from appium.webdriver.extensions.flutter_integration.scroll_directions import ScrollDirection
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement


class FlutterCommand:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    # wait commands

    def wait_for_visible(
        self,
        locator: Union[WebElement, FlutterFinder],
        timeout: Optional[float] = None,
    ) -> None:
        """
        Waits for a element to become visible.

        Args:
            locator (Union[WebElement, FlutterFinder]): The element to wait for; can be a WebElement or a FlutterFinder.
            timeout (Optional[float]): Maximum wait time in seconds. Defaults to a predefined timeout if not specified.

        Returns:
            None:
        """
        opts: Dict[str, Any] = self.__get_locator_options(locator)
        if timeout is not None:
            opts['timeout'] = timeout

        self.execute_flutter_command('waitForVisible', opts)

    def wait_for_invisible(
        self,
        locator: Union[WebElement, FlutterFinder],
        timeout: Optional[float] = None,
    ) -> None:
        """
        Waits for a element to become invisible.

        Args:
            locator (Union[WebElement, FlutterFinder]): The element to wait for; can be a WebElement or a FlutterFinder.
            timeout (Optional[float]): Maximum wait time in seconds. Defaults to a predefined timeout if not specified.

        Returns:
            None:
        """
        opts: Dict[str, Any] = self.__get_locator_options(locator)
        if timeout is not None:
            opts['timeout'] = timeout

        self.execute_flutter_command('waitForAbsent', opts)

    # flutter action commands

    def perform_double_click(self, element: WebElement, offset: Optional[Tuple[int, int]] = None) -> None:
        """
        Performs a double-click on the given element, with an optional offset.

        Args:
            element (WebElement): The element to double-click on. This parameter is required.
            offset (Optional[Tuple[int, int]]): The x and y offsets from the element to click at. If not specified, the click is performed at the element's center.

        Returns:
            None:
        """
        opts: Dict[str, Union[WebElement, Dict[str, int]]] = {'origin': element}
        if offset is not None:
            opts['offset'] = {'x': offset[0], 'y': offset[1]}
        self.execute_flutter_command('doubleClick', opts)

    def perform_long_press(self, element: WebElement, offset: Optional[Tuple[int, int]] = None) -> None:
        """
        Performs a long press on the given element, with an optional offset.

        Args:
            element (WebElement): The element to perform the long press on. This parameter is required.
            offset (Optional[Tuple[int, int]]): The x and y offsets from the element to perform the long press at. If not specified, the long press is performed at the element's center.

        Returns:
            None:
        """
        opts: Dict[str, Union[WebElement, Dict[str, int]]] = {'origin': element}
        if offset is not None:
            opts['offset'] = {'x': offset[0], 'y': offset[1]}
        self.execute_flutter_command('longPress', opts)

    def perform_drag_and_drop(self, source: WebElement, target: WebElement) -> None:
        """
        Performs a drag-and-drop operation from a source element to a target element.

        Args:
            source (WebElement): The element to drag from.
            target (WebElement): The element to drop onto.

        Returns:
            None:
        """
        self.execute_flutter_command('dragAndDrop', {'source': source, 'target': target})

    def scroll_till_visible(
        self,
        scroll_to: FlutterFinder,
        scroll_direction: ScrollDirection = ScrollDirection.DOWN,
        **opts: Any,
    ) -> WebElement:
        """
        Scrolls until the specified element becomes visible.

        Args:
            scroll_to (FlutterFinder): The Flutter element to scroll to.
            scroll_direction (ScrollDirection): The direction to scroll up or down. Defaults to `ScrollDirection.DOWN`.

        KeywordArgs:
                scrollView (str): The view of the scroll. Default value is 'Scrollable'
                delta (int): delta for the scroll. Default value is 64
                maxScrolls (int): Max times to scroll. Default value is 15
                settleBetweenScrollsTimeout (float): settle timeout in milliseconds. Default value is 5000
                dragDuration (float): time gap between each scroll in milliseconds. Default value is 100

        Returns:
            Webelement: scrolled element
        """
        opts['finder'] = scroll_to.to_dict()
        opts['scrollDirection'] = scroll_direction.value
        return self.execute_flutter_command('scrollTillVisible', opts)

    def inject_mock_image(self, value: str) -> str:
        """
        Injects a mock image to the device. The input can be a file path or a base64-encoded string.

        Args:
            value (str): The file path of the image or a base64-encoded string.

        Returns:
            str: Image ID of the injected image.
        """
        if os.path.isfile(value):
            base64_encoded_image = encode_file_to_base64(value)
        else:
            base64_encoded_image = value
        return self.execute_flutter_command('injectImage', {'base64Image': base64_encoded_image})

    def activate_injected_image(self, image_id: str) -> None:
        """
        Activates an injected image with image ID.

        Args:
            image_id (str): The ID of the injected image to activate.

        Returns:
            None:
        """
        self.execute_flutter_command('activateInjectedImage', {'imageId': image_id})

    def execute_flutter_command(self, scriptName: str, params: dict) -> Any:
        """
        Executes a Flutter command by sending a script and parameters to the flutter integration driver.

        Args:
            scriptName (str): The name of the Flutter command to execute.
                This will be prefixed with 'flutter:' when passed to the driver.
            params (dict): A dictionary of parameters to be passed along with the Flutter command.

        Returns:
            Any: The result of the command execution. The return value depends on the
            specific Flutter command being executed.
        """
        return self.driver.execute_script(f'flutter: {scriptName}', params)

    def __get_locator_options(self, locator: Union[WebElement, 'FlutterFinder']) -> Dict[str, dict]:
        if isinstance(locator, WebElement):
            return {'element': locator}
        return {'locator': locator.to_dict()}
