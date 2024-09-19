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
from typing import Any, Optional, Tuple, Union
from appium.webdriver.flutter_finder import FlutterFinder
from appium.webdriver.webdriver import WebDriver
from appium.webdriver.webelement import WebElement


class FlutterCommand():
    
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        
     # wait commands   
     
    def wait_for_visible(self, locator: Union[WebElement, FlutterFinder], time_out: Optional[int] = None) -> None:
        """
        Waits for a element to become visible.

        Args:
            locator: The element to wait for; can be a WebElement or a FlutterFinder.
            time_out: Maximum wait time in seconds. Defaults to a predefined timeout if not specified.
            
        Returns: 
            None: 
        """
        if isinstance(locator, WebElement):
            opts = {'element': locator, 'timeout': time_out}
        else:
            opts = {'locator': locator.to_dict(), 'timeout': time_out}

        self.execute_flutter_command('waitForVisible', opts)

            
    def wait_for_invisible(self, locator: Union[WebElement, FlutterFinder], time_out: Optional[int] = None) -> None:
        """
        Waits for a element to become invisible.

        Args:
            locator: The element to wait for; can be a WebElement or a FlutterFinder.
            time_out: Maximum wait time in seconds. Defaults to a predefined timeout if not specified.
            
        Returns:
            None: 
        """
        if isinstance(locator, WebElement):
            opts = {'element': locator, 'timeout': time_out}
        else:
            opts = {'locator': locator.to_dict(), 'timeout': time_out}
        
        self.execute_flutter_command('waitForAbsent', opts)

    # flutter action commands
    
    def perform_double_click(self, element: WebElement, offset: Optional[Tuple[int, int]] = None) -> None:
        """
        Performs a double-click on the given element, with an optional offset.

        Args:
            element: The element to double-click on. This parameter is required.
            offset: The x and y offsets from the element to click at. If not specified, the click is performed at the element's center.
            
        Returns:
            None:
        """
        opts = {'origin': element}
        if offset:
            opts['offset'] = {'x': offset[0], 'y': offset[1]}
        self.execute_flutter_command('doubleClick', opts)
    
    def perform_long_press(self, element: WebElement, offset: Optional[Tuple[int, int]] = None) -> None:
        """
        Performs a long press on the given element, with an optional offset.

        Args:
            element: The element to perform the long press on. This parameter is required.
            offset: The x and y offsets from the element to perform the long press at. If not specified, the long press is performed at the element's center.
            
        Returns:
            None:
        """
        opts = {'origin': element}
        if offset:
            opts['offset'] = {'x': offset[0], 'y': offset[1]}
        self.execute_flutter_command('longPress', opts)
            
    def perform_drag_and_drop(self, source: WebElement, target: WebElement) -> None:
        """
        Performs a drag-and-drop operation from a source element to a target element.

        Args:
            source: The element to drag from.
            target: The element to drop onto.
            
        Returns:
            None:
        """
        self.execute_flutter_command('dragAndDrop', {'source': source, 'target': target})
        
    def scroll_till_visible(self, scroll_to: FlutterFinder, scroll_direction: Optional[str] = 'down', **opts: Any) -> WebElement:
        """
        Scrolls until the specified element becomes visible.

        Args:
            scroll_to: The Flutter element to scroll to.
            scroll_direction: The direction to scroll up/down. Defaults to 'down'.
                
        KeywordArgs:
                scrollView (str): The view of the scroll.
                delta (int): delta for the scroll
                maxScrolls (int): Max times to scroll
                settleBetweenScrollsTimeout (int): settle timeout
                dragDuration (int): time gap between each scroll
        
        Returns:
            Webelement: scrolled element
        """
        opts['finder'] = scroll_to.to_dict()
        opts['scrollDirection'] = scroll_direction
        return self.execute_flutter_command('scrollTillVisible', opts)
        
    def inject_mock_image(self, value: str) -> str:
        """
        Injects a mock image to the device. The input can be a file path or a base64-encoded string.

        Args:
            value: The file path of the image or a base64-encoded string.
            
        Returns:
            str: Image ID of the injected image.
        """
        import os
        if os.path.isfile(value):        
            with open(value, "rb") as image_file:
                base64_encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        else:
            base64_encoded_image = value
        return self.execute_flutter_command('injectImage', {'base64Image': base64_encoded_image})
    
    def activate_injected_image(self, image_id: str) -> None:
        """
        Activates an injected image with image ID.

        Args:
            image_id: The ID of the injected image to activate.

        Returns:
            None:
        """
        self.execute_flutter_command("activateInjectedImage", {'imageId': image_id})
        
    def execute_flutter_command(self, scriptName: str, params: dict) -> Any:
        return self.driver.execute_script(f'flutter: {scriptName}', params)