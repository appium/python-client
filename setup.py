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

# FIXME: Remove this setup.py completely.
# Then, we should bump the major version since the package will not include setup.py.

try:
    # Python 3.11+
    import tomllib
except Exception:
    # for older versions
    import tomli as tomllib

with open('pyproject.toml', 'rb') as f:
    pyproject = tomllib.load(f)
    project = pyproject['project']

from setuptools import find_packages, setup

setup(
    name=project['name'],
    version=project['version'],
    description=project['description'],
    keywords=project['keywords'],
    author=project['authors'][0]['name'],
    author_email=project['authors'][0]['email'],
    maintainer=', '.join([maintainer['name'] for maintainer in project['maintainers']]),
    url=project['urls']['Homepage'],
    package_data={'appium': ['py.typed']},
    packages=find_packages(include=['appium*']),
    license=project['license'],
    classifiers=project['classifiers'],
    install_requires=project['dependencies'],
)
