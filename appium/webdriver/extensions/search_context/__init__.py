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

# pylint: disable=abstract-method

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement

from .android import AndroidSearchContext
from .custom import CustomSearchContext
from .ios import iOSSearchContext
from .mobile import MobileSearchContext
from .windows import WindowsSearchContext


class AppiumSearchContext(
    webdriver.Remote,
    AndroidSearchContext,
    CustomSearchContext,
    iOSSearchContext,
    MobileSearchContext,
    WindowsSearchContext,
):
    """Returns appium driver search conext"""


class AppiumWebElementSearchContext(
    SeleniumWebElement,
    AndroidSearchContext,
    CustomSearchContext,
    iOSSearchContext,
    MobileSearchContext,
    WindowsSearchContext,
):
    """Returns appium web element search context"""
