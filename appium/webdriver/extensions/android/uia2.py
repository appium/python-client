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

from typing import TYPE_CHECKING, Optional, TypeVar, Union

from selenium import webdriver

from appium.webdriver.mobilecommand import MobileCommand as Command

if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from appium.webdriver.webdriver import WebDriver
    from appium.webdriver.webelement import WebElement

T = TypeVar('T', bound=Union['WebDriver', 'Uia2'])


class Uia2(webdriver.Remote):

    def flick_uia2(self, element: Optional['WebElement'] = None,
                   xspeed: int = 0, yspeed: int = 0,
                   xoffset: int = 0, yoffset: int = 0,
                   speed: int = 0) -> T:
        """Flick the element

        Args:
            element: the element to be flicked
            xoffset: used for the flick endpoint (endpoint: element x pos + xoffset)
            yoffset: used for the flick endpoint (endpoint: element y pos + yoffset)
            speed: flick speed

            xspeed: (Used when element is not set) flick speed for vertical direction
            yspeed: (Used when element is not set) flick speed for horizontal direction

        Usage:
            # When element is set
            el = driver.find_element_by_accessibility_id('Grid')
            driver.flick_uia2(el, xoffset=0, yoffset=-100, speed=100)

            # When element is not set
            driver.flick_uia2(xspeed=100, yspeed=-100)

        Returns:
            `appium.webdriver.webdriver.WebDriver`: Self instance
        """

        data = {}
        if element is None:
            data = {
                'xspeed': xspeed,
                'yspeed': yspeed,
            }
        else:
            data = {
                'element': element.id,
                'xoffset': xoffset,
                'yoffset': yoffset,
                'speed': speed
            }

        self.execute(Command.FLICK_ELEMENT, data)
        return self

    # pylint: disable=protected-access
    # noinspection PyProtectedMember
    def _addCommands(self) -> None:
        self.command_executor._commands[Command.FLICK_ELEMENT] = \
            ('POST', '/session/$sessionId/touch/flick')
