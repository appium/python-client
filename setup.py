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
import io
import os

from distutils.core import setup
from setuptools import setup
from appium.common.helper import library_version

setup(
    name='Appium-Python-Client',
    version=library_version(),
    description='Python client for Appium',
    long_description=io.open(os.path.join(os.path.dirname('__file__'), 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    keywords=[
        'appium',
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
        'appium.webdriver.common',
        'appium.webdriver.extensions'
    ],
    license='Apache 2.0',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
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
