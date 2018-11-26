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
from script.helper import read_version

VERSION_FILE_PATH = os.path.join(os.path.dirname('__file__'), 'appium', 'version.py')
CHANGELOG_PATH = os.path.join(os.path.dirname('__file__'), 'CHANGELOG.rst')


def get_current_version():
    current = read_version()
    print('The current version is \033[1;33m{}\033[0m, type a new one'.format(current))
    return current


def get_new_version():
    print('\033[1;32mnew version:\033[0m')
    for line in sys.stdin:
        return line.rstrip()


VERSION_FORMAT = "version = '{}'"


def update_version_file(version):
    new_version = VERSION_FORMAT.format(version)
    with open(VERSION_FILE_PATH, 'w') as f:
        f.write(new_version)


def call_bash_script(cmd):
    if os.environ.get('DRY_RUN') is not None:
        print('\033[1;31m[DRY_RUN]\033[0m Calls: {}'.format(cmd))
    else:
        os.system(cmd)


def commit_version_code(new_version_num):
    call_bash_script('git commit {} -m "Bump {}"'.format(VERSION_FILE_PATH, new_version_num))


def tag_and_generate_changelog(new_version_num):
    call_bash_script('git tag "v{}"'.format(new_version_num))
    call_bash_script('gitchangelog > {}'.format(CHANGELOG_PATH))
    call_bash_script('git commit {} -m "Update changelog for {}"'.format(CHANGELOG_PATH, new_version_num))


def upload_sdist(new_version_num):
    call_bash_script('twine upload "dist/Appium-Python-Client-{}.tar.gz"'.format(new_version_num))


def push_changes_to_master(new_version_num):
    call_bash_script('git push origin master')
    call_bash_script('git push origin "v{}"'.format(new_version_num))


def ensure_publication(new_version_num):
    if os.environ.get('DRY_RUN') is not None:
        print('Run with \033[1;31m[DRY_RUN]\033[0m mode.')

    print('Are you sure to release as \033[1;33mv{}\033[0m?[y/n]'.format(new_version_num))
    for line in sys.stdin:
        if line.rstrip().lower() == 'y':
            return
        exit('Canceled release pricess.')


def build_sdist():
    call_bash_script('{} setup.py sdist'.format(sys.executable))


def validate_release_env():
    if os.system('which twine') != 0:
        exit("Please get twine via 'pip install twine'")
    if os.system('which gitchangelog') != 0:
        exit("Please get twine via 'pip install gitchangelog' or 'pip install git+git://github.com/vaab/gitchangelog.git' for Python 3.7")


def main():
    validate_release_env()

    get_current_version()
    new_version = get_new_version()

    update_version_file(new_version)

    ensure_publication(new_version)

    commit_version_code(new_version)
    build_sdist()

    tag_and_generate_changelog(new_version)

    upload_sdist(new_version)
    push_changes_to_master(new_version)


if __name__ == '__main__':
    main()
