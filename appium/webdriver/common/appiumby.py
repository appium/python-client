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

from typing import Literal

from selenium.webdriver.common.by import By

ByType = Literal[
    '-ios predicate string',
    '-ios class chain',
    '-android uiautomator',
    '-android viewtag',
    '-android datamatcher',
    '-android viewmatcher',
    'accessibility id',
    '-image',
    '-custom',
    '-flutter semantics label',
    '-flutter type',
    '-flutter key',
    '-flutter text',
    '-flutter text containing',
]


class AppiumBy(By):
    IOS_PREDICATE: ByType = '-ios predicate string'
    IOS_CLASS_CHAIN: ByType = '-ios class chain'
    ANDROID_UIAUTOMATOR: ByType = '-android uiautomator'
    ANDROID_VIEWTAG: ByType = '-android viewtag'
    ANDROID_DATA_MATCHER: ByType = '-android datamatcher'
    ANDROID_VIEW_MATCHER: ByType = '-android viewmatcher'
    ACCESSIBILITY_ID: ByType = 'accessibility id'
    IMAGE: ByType = '-image'
    CUSTOM: ByType = '-custom'

    # For Flutter integration usage https://github.com/AppiumTestDistribution/appium-flutter-integration-driver/tree/main
    FLUTTER_INTEGRATION_SEMANTICS_LABEL: ByType = '-flutter semantics label'
    FLUTTER_INTEGRATION_TYPE: ByType = '-flutter type'
    FLUTTER_INTEGRATION_KEY: ByType = '-flutter key'
    FLUTTER_INTEGRATION_TEXT: ByType = '-flutter text'
    FLUTTER_INTEGRATION_TEXT_CONTAINING: ByType = '-flutter text containing'
