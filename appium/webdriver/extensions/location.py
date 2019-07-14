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


class Location(webdriver.Remote):
    def toggle_location_services(self):
        """Toggle the location services on the device.

        Android only.

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        self.execute(Command.TOGGLE_LOCATION_SERVICES, {})
        return self

    def set_location(self, latitude, longitude, altitude=None):
        """Set the location of the device

        Args:
            latitude (Union[float, str]): String or numeric value between -90.0 and 90.00
            longitude (Union[float, str]): String or numeric value between -180.0 and 180.0
            altitude (Union[float, str], optional): String or numeric value (Android real device only)

        Returns:
            `appium.webdriver.webdriver.WebDriver`
        """
        data = {
            "location": {
                "latitude": latitude,
                "longitude": longitude,
            }
        }
        if altitude is not None:
            data['location']['altitude'] = altitude
        self.execute(Command.SET_LOCATION, data)
        return self

    @property
    def location(self):
        """Retrieves the current location

        Returns:
            A dictionary whose keys are
             - latitude (float)
             - longitude (float)
             - altitude (float)
        """
        return self.execute(Command.GET_LOCATION)['value']

    # pylint: disable=protected-access

    def _addCommands(self):
        self.command_executor._commands[Command.TOGGLE_LOCATION_SERVICES] = \
            ('POST', '/session/$sessionId/appium/device/toggle_location_services')
        self.command_executor._commands[Command.GET_LOCATION] = \
            ('GET', '/session/$sessionId/location')
        self.command_executor._commands[Command.SET_LOCATION] = \
            ('POST', '/session/$sessionId/location')
