# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from appium.webdriver.common.flutterby import FlutterBy

class FlutterFinder():
    
    def __init__(self, using: str, value: str) -> None:
        self.using = using
        self.value = value
    
    @staticmethod
    def by_flutter_key(value: str) -> 'FlutterFinder':
        return FlutterFinder(FlutterBy.FLUTTER_KEY,  value)
    
    @staticmethod
    def by_flutter_text(value: str) -> 'FlutterFinder':
        return FlutterFinder(FlutterBy.FLUTTER_TEXT,  value)
    
    @staticmethod
    def by_flutter_semantics_label(value: str) -> 'FlutterFinder':
        return FlutterFinder(FlutterBy.FLUTTER_SEMANTICS_LABEL,  value)
    
    @staticmethod
    def by_flutter_type(value: str) -> 'FlutterFinder':
        return FlutterFinder(FlutterBy.FLUTTER_TYPE,  value)
    
    @staticmethod
    def by_flutter_text_containing(value: str) -> 'FlutterFinder':
        return FlutterFinder(FlutterBy.FLUTTER_TEXT_CONTAINING,  value)
    
    def to_dict(self):
        return { "using": self.using, "value": self.value} 
    
    def as_strings(self) -> str:
        return self.using, self.value
        
