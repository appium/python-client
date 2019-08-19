#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import httpretty

from test.unit.helper.test_helper import (
    android_w3c_driver,
    appium_command,
    get_httpretty_request_body
)


class TestWebDriverScreenRecord(object):

    @httpretty.activate
    def test_start_recording_screen(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/start_recording_screen'),
        )
        assert driver.start_recording_screen(user='userA', password='12345') is None

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['options']['user'] == 'userA'
        assert d['options']['pass'] == '12345'
        assert 'password' not in d['options'].keys()

    @httpretty.activate
    def test_stop_recording_screen(self):
        driver = android_w3c_driver()
        httpretty.register_uri(
            httpretty.POST,
            appium_command('/session/1234567890/appium/stop_recording_screen'),
            body='{"value": "b64_video_data"}'
        )
        assert driver.stop_recording_screen(user='userA', password='12345') == 'b64_video_data'

        d = get_httpretty_request_body(httpretty.last_request())
        assert d['options']['user'] == 'userA'
        assert d['options']['pass'] == '12345'
        assert 'password' not in d['options'].keys()
