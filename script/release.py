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
"""Release script to publish release module to pipy."""

import os
import sys

CHANGELOG_PATH = os.path.join(os.path.dirname('__file__'), 'CHANGELOG.md')

APPIUM_DIR_PATH = os.path.join(os.path.dirname('__file__'), 'appium')
BUILT_APPIUM_DIR_PATH = os.path.join(os.path.dirname('__file__'), 'build', 'lib', 'appium')

MESSAGE_RED = '\033[1;31m{}\033[0m'
MESSAGE_GREEN = '\033[1;32m{}\033[0m'
MESSAGE_YELLOW = '\033[1;33m{}\033[0m'


def print_current_version():
    os.system('uv version')


def get_new_version():
    print(MESSAGE_GREEN.format('Pushing version:'))
    for line in sys.stdin:
        return line.rstrip()


def call_bash_script(cmd):
    if os.environ.get('DRY_RUN') is not None:
        print('{} Calls: {}'.format(MESSAGE_RED.format('[DRY_RUN]'), cmd))
    else:
        os.system(cmd)


def upload_sdist(new_version_num):
    wheel_file = 'dist/appium_python_client-{}-py3-none-any.whl'.format(new_version_num)
    push_file = 'dist/appium_python_client-{}.tar.gz'.format(new_version_num)
    try:
        call_bash_script(f"uv run twine upload '{wheel_file}' '{push_file}'")
    except Exception as e:
        print(
            'Failed to upload {} to pypi. Please fix the original error and push it again later. Original error: {}'.format(
                push_file, e
            )
        )


def ensure_publication(new_version_num):
    if os.environ.get('DRY_RUN') is not None:
        print('Run with {} mode.'.format(MESSAGE_RED.format('[DRY_RUN]')))

    print(
        'Are you sure to publish a new built modules in dist directory as {}?[y/n]'.format(
            MESSAGE_YELLOW.format(new_version_num)
        )
    )
    for line in sys.stdin:
        if line.rstrip().lower() == 'y':
            return
        sys.exit('Canceled release process.')


def main():
    print_current_version()
    new_version = get_new_version()

    ensure_publication(new_version)

    upload_sdist(new_version)


if __name__ == '__main__':
    main()
