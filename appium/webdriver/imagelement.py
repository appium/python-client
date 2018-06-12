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

import math


class ImageElement:

    def __init__(self, driver, x, y, width, height):
        self.driver = driver
        self.center_x = math.floor(x + width / 2)
        self.center_y = math.floor(y + height / 2)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def click(self):
        """
        Clicks in the middle of an image bounds
        """
        return self.driver.tap([(self.center_x, self.center_y)])

    @property
    def size(self):
        return {'width': self.width, 'height': self.height}

    @property
    def location(self):
        return {'x': self.x, 'y': self.y}

    @property
    def rect(self):
        return {
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def is_displayed(self):
        return True
