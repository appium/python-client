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

from selenium.webdriver.common.by import By


class MobileBy(By):
    IOS_PREDICATE = '-ios predicate string'
    IOS_UIAUTOMATION = '-ios uiautomation'
    IOS_CLASS_CHAIN = '-ios class chain'
    ANDROID_UIAUTOMATOR = '-android uiautomator'
    ANDROID_VIEWTAG = '-android viewtag'
    ANDROID_DATA_MATCHER = '-android datamatcher'
    ANDROID_VIEW_MATCHER = '-android viewmatcher'
    WINDOWS_UI_AUTOMATION = '-windows uiautomation'
    ACCESSIBILITY_ID = 'accessibility id'
    IMAGE = '-image'
    CUSTOM = '-custom'
