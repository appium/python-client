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
import io

from distutils.core import setup
from setuptools import setup

def read_version():
    ctx = {}
    exec(local_file('appium', 'version.py'), ctx)
    return ctx['version']

local_file = lambda *f: \
    io.open(
        os.path.join(os.path.dirname('__file__'), *f), encoding='utf-8').read()

setup(
    name='Appium-Python-Client',
    version=read_version(),
    description='Python client for Appium 1.5',
    keywords=[
        'appium',
        'appium 1.0',
        'selenium',
        'selenium 3',
        'python client',
        'mobile automation'
    ],
    author='Isaac Murchie',
    author_email='isaac@saucelabs.com',
    url='http://appium.io/',
    packages=[
        'appium',
        'appium.common',
        'appium.webdriver',
        'appium.webdriver.common'
    ],
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing'
    ],
    install_requires=['selenium>=3.14.1']
)
