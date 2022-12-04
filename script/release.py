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

import glob
import io
import os
import shutil
import subprocess
import sys
from typing import List

VERSION_FILE_PATH = os.path.join(os.path.dirname('__file__'), 'appium', 'version.py')
CHANGELOG_PATH = os.path.join(os.path.dirname('__file__'), 'CHANGELOG.rst')

APPIUM_DIR_PATH = os.path.join(os.path.dirname('__file__'), 'appium')
BUILT_APPIUM_DIR_PATH = os.path.join(os.path.dirname('__file__'), 'build', 'lib', 'appium')

MESSAGE_RED = '\033[1;31m{}\033[0m'
MESSAGE_GREEN = '\033[1;32m{}\033[0m'
MESSAGE_YELLOW = '\033[1;33m{}\033[0m'


def get_current_version():
    current = (
        io.open(os.path.join(os.path.dirname('__file__'), 'appium', 'version.py'), encoding='utf-8').read().rstrip()
    )
    print(f'The current version is {MESSAGE_YELLOW.format(current)}, type a new one')
    return current


def get_new_version():
    print(MESSAGE_GREEN.format('new version:'))
    for line in sys.stdin:
        return line.rstrip()


VERSION_FORMAT = "version = '{}'\n"


def update_version_file(version):
    new_version = VERSION_FORMAT.format(version)
    with open(VERSION_FILE_PATH, 'w', encoding="utf-8") as f:
        f.write(new_version)


def call_bash_script(cmd):
    if os.environ.get('DRY_RUN') is not None:
        print(f"{MESSAGE_RED.format('[DRY_RUN]')} Calls: {cmd}")
    else:
        os.system(cmd)


def commit_version_code(new_version_num):
    call_bash_script(f'git commit {VERSION_FILE_PATH} -m "Bump {new_version_num}"')


def tag_and_generate_changelog(new_version_num):
    call_bash_script(f'git tag "v{new_version_num}"')
    call_bash_script(f'gitchangelog > {CHANGELOG_PATH}')
    call_bash_script(f'git commit {CHANGELOG_PATH} -m "Update changelog for {new_version_num}"')


def upload_sdist(new_version_num):
    push_file = f'dist/Appium-Python-Client-{new_version_num}.tar.gz'
    try:
        call_bash_script(f'twine upload "{push_file}"')
    except Exception as e:
        print(
            f'Failed to upload {push_file} to pypi. '
            f'Please fix the original error and push it again later. Original error: {e}'
        )


def push_changes_to_master(new_version_num):
    call_bash_script('git push origin master')
    call_bash_script(f'git push origin "v{new_version_num}"')


def ensure_publication(new_version_num):
    if os.environ.get('DRY_RUN') is not None:
        print(f"Run with {MESSAGE_RED.format('[DRY_RUN]')} mode.")

    print(f'Are you sure to release as {MESSAGE_YELLOW.format(new_version_num)}?[y/n]')
    for line in sys.stdin:
        if line.rstrip().lower() == 'y':
            return
        sys.exit('Canceled release process.')


def build_sdist():
    call_bash_script(f'{sys.executable} setup.py sdist')


def validate_release_env():
    if os.system('which twine') != 0:
        sys.exit("Please get twine via 'pip install twine'")
    if os.system('which gitchangelog') != 0:
        sys.exit(
            "Please get twine via 'pip install gitchangelog' or 'pip install git+git://github.com/vaab/gitchangelog.git' for Python 3.7"
        )


def build() -> None:
    shutil.rmtree(BUILT_APPIUM_DIR_PATH, ignore_errors=True)
    status, output = subprocess.getstatusoutput(f"{os.getenv('PYTHON_BIN_PATH')} setup.py install")
    if status != 0:
        sys.exit(f'Failed to build the package:\n{output}')


def get_py_files_in_dir(root_dir: str) -> List[str]:
    return [
        file_path[len(root_dir) :]
        for file_path in glob.glob(f"{root_dir}/**/*.py", recursive=True)
        + glob.glob(f"{root_dir}/**/*.typed", recursive=True)
    ]


def assert_files_count_in_package() -> None:
    original_files = get_py_files_in_dir(APPIUM_DIR_PATH)
    built_files = get_py_files_in_dir(BUILT_APPIUM_DIR_PATH)

    if len(original_files) != len(built_files):
        print(f"The count of files in '{APPIUM_DIR_PATH}' and '{BUILT_APPIUM_DIR_PATH}' were different.")

        original_files_set = set(original_files)
        built_files_set = set(built_files)

        diff = original_files_set.difference(built_files_set)
        if diff:
            print(f"'{APPIUM_DIR_PATH}' has '{diff}' files than {BUILT_APPIUM_DIR_PATH}")
        diff = built_files_set.difference(original_files_set)
        if diff:
            print(f"{BUILT_APPIUM_DIR_PATH} has {diff} files than {APPIUM_DIR_PATH}")

        sys.exit(
            f"Python files in '{BUILT_APPIUM_DIR_PATH}' may differ from '{APPIUM_DIR_PATH}'. "
            "Please make sure setup.py is configured properly."
        )


def main():
    validate_release_env()

    get_current_version()
    new_version = get_new_version()

    update_version_file(new_version)

    build()
    assert_files_count_in_package()

    ensure_publication(new_version)

    commit_version_code(new_version)
    build_sdist()

    tag_and_generate_changelog(new_version)

    upload_sdist(new_version)
    push_changes_to_master(new_version)


if __name__ == '__main__':
    main()
