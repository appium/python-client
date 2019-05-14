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

import base64
import os
import random
import unittest
from zipfile import ZipFile

from appium import webdriver
from appium.common.helper import appium_bytes
import desired_capabilities


class RemoteFsTests(unittest.TestCase):
    def setUp(self):
        desired_caps = desired_capabilities.get_desired_capabilities('ApiDemos-debug.apk')
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

        # remove zipped file from `test_pull_folder`
        if os.path.isfile(getattr(self, 'zipfilename', '')):
            os.remove(self.zipfilename)

    def test_push_pull_file(self):
        dest_path = '/data/local/tmp/test_push_file.txt'
        data = appium_bytes('This is the contents of the file to push to the device.', 'utf-8')

        self.driver.push_file(dest_path, base64.b64encode(data).decode('utf-8'))
        data_ret = base64.b64decode(self.driver.pull_file(dest_path))

        self.assertEqual(data, data_ret)

    def test_pull_folder(self):
        data = appium_bytes('random string data {}'.format(random.randint(0, 1000)), 'utf-8')
        dest_dir = '/data/local/tmp/'

        for filename in ['1.txt', '2.txt']:
            self.driver.push_file(os.path.join(dest_dir, filename), base64.b64encode(data).decode('utf-8'))

        folder = self.driver.pull_folder(dest_dir)

        # python doesn't have any functionality for unzipping streams
        # save temporary file, which will be deleted in `tearDown`
        self.zipfilename = 'folder_%d.zip' % random.randint(0, 1000000)
        with open(self.zipfilename, "wb") as fw:
            fw.write(base64.b64decode(folder))

        with ZipFile(self.zipfilename, 'r') as myzip:
            # should find these. otherwise it will raise a `KeyError`
            for filename in ['1.txt', '2.txt']:
                myzip.read(filename)

    def test_push_file_with_src_path(self):
        test_files = ['test_image.jpg', 'test_file.txt']
        for file_name in test_files:
            src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
            dest_path = os.path.join('/data/local/tmp/', file_name)

            with open(src_path, 'rb') as fr:
                original_data = fr.read()

            self.driver.push_file(dest_path, source_path=src_path)
            new_data = base64.b64decode(self.driver.pull_file(dest_path))
            self.assertEqual(original_data, new_data)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(RemoteFsTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
