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


import httplib
import os
import subprocess
import sys
import time


DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 4723
STARTUP_TIMEOUT_MS = 60000
MAIN_SCRIPT_PATH = 'appium/build/lib/main.js'


def find_executable(executable):
    path = os.environ['PATH']
    paths = path.split(os.pathsep)
    base, ext = os.path.splitext(executable)

    if sys.platform == 'win32' and ext.lower() != '.exe':
        executable = executable + '.exe'

    if os.path.isfile(executable):
        return executable

    for p in paths:
        full_path = os.path.join(p, executable)
        if os.path.isfile(full_path):
            return full_path

    return None


def poll_url(host, port, path, timeout_ms):
    time_started_sec = time.time()
    while time.time() < time_started_sec + timeout_ms / 1000.0:
        try:
            conn = httplib.HTTPConnection(host=host, port=port, timeout=1.0)
            conn.request('HEAD', path)
            if conn.getresponse().status < 400:
                return True
        except Exception:
            pass
        time.sleep(1.0)
    return False


class AppiumServiceError(RuntimeError):
    pass


class AppiumService(object):
    def __init__(self):
        self._process = None

    def _get_node(self):
        if not hasattr(self, '_node_executable'):
            self._node_executable = find_executable('node')
        if self._node_executable is None:
            raise AppiumServiceError('NodeJS main executable cannot be found. ' +
                                     'Make sure it is installed and present in PATH')
        return self._node_executable

    def _get_npm(self):
        if not hasattr(self, '_npm_executable'):
            self._npm_executable = find_executable('npm')
        if self._npm_executable is None:
            raise AppiumServiceError('Node Package Manager executable cannot be found. ' +
                                     'Make sure it is installed and present in PATH')
        return self._npm_executable

    def _get_main_script(self):
        if not hasattr(self, '_main_script'):
            for args in [['root', '-g'], ['root']]:
                try:
                    modules_root = subprocess.check_output([self._get_npm()] + args).strip()
                    if os.path.exists(os.path.join(modules_root, MAIN_SCRIPT_PATH)):
                        self._main_script = os.path.join(modules_root, MAIN_SCRIPT_PATH)
                        break
                except subprocess.CalledProcessError:
                    continue
            if not hasattr(self, '_main_script'):
                try:
                    self._main_script = subprocess.check_output(
                        [self._get_node(),
                         '-e',
                         'console.log(require.resolve("{}"))'.format(MAIN_SCRIPT_PATH)]).strip()
                except subprocess.CalledProcessError as e:
                    raise AppiumServiceError(e.output)
        return self._main_script

    @staticmethod
    def _parse_port_number(args):
        for idx, arg in enumerate(args or []):
            if arg == '--port' and idx < len(args) - 1:
                return int(args[idx + 1])
        return DEFAULT_PORT

    @staticmethod
    def _parse_host(args):
        for idx, arg in enumerate(args or []):
            if arg == '--host' and idx < len(args) - 1:
                return args[idx + 1]
        return DEFAULT_HOST

    def start(self, **kwargs):
        """
        Starts Appium service with given arguments.
        The service will be forcefully restarted if it is already running.

        :param kwargs:
        `env` - Environment variables mapping. The default system environment,
        which is inherited from the parent process is assigned by default.
        `node` - The full path to the main NodeJS executable. The service will try
        to retrieve it automatically by default.
        `stdout` - Check on the documentation for subprocess.Popen for more details.
        The default value is subprocess.PIPE.
        `stderr` - Check on the documentation for subprocess.Popen for more details.
        The default value is subprocess.PIPE.
        `timeout_ms` - The maximum time to wait until Appium process starts listening
        for HTTP connections. If set to 0 or negative number then no wait will be applied.
        60000 ms by default
        `main_script` - The full path to the main Appium executable
        (usually located this is build/lib/main.js). If this is not set
        then the service tries to detect the path automatically.
        `args` - List of Appium arguments. Check on
        https://appium.io/docs/en/writing-running-appium/server-args/ for more details
        about possible arguments and their values.
        :return:
        subprocess.Popen instance. You can use Popen.communicate interface
        (stdout and stderr must be set to subprocess.PIPE in such case)
        in order to retrieve the actual process output.
        """
        self.stop()

        env = kwargs['env'] if 'env' in kwargs else None
        node = kwargs['node'] if 'node' in kwargs else self._get_node()
        stdout = kwargs['stdout'] if 'stdout' in kwargs else subprocess.PIPE
        stderr = kwargs['stderr'] if 'stderr' in kwargs else subprocess.PIPE
        timeout_ms = int(kwargs['timeout_ms']) if 'timeout_ms' in kwargs else STARTUP_TIMEOUT_MS
        main_script = kwargs['main_script'] if 'main_script' in kwargs else self._get_main_script()
        args = [node, main_script]
        if 'args' in kwargs:
            args.extend(kwargs['args'])
        self._process = subprocess.Popen(args=args, stdout=stdout, stderr=stderr, env=env)
        if timeout_ms > 0:
            host = self._parse_host(args)
            port = self._parse_port_number(args)
            error_msg = None
            if not poll_url(host, port, '/wd/hub/status', timeout_ms):
                error_msg = 'Appium has failed to start on {}:{} within {}ms timeout'.format(host, port, timeout_ms)
            if not self.is_running():
                error_msg = 'Appium has failed to start on {}:{} within {}ms timeout. ' + \
                            'Make sure the port #{} is not occupied by other applications'\
                            .format(host, port, timeout_ms, port)
            if error_msg is not None:
                if stderr == subprocess.PIPE:
                    err_output = self._process.communicate()[1]
                    if err_output:
                        error_msg += '. Original error: {}'.format(err_output)
                raise AppiumServiceError(error_msg)
        return self._process

    def stop(self):
        if self.is_running():
            self._process.terminate()
        self._process = None

    def is_running(self):
        return self._process is not None and self._process.poll() is None


if __name__ == '__main__':
    assert(find_executable('node') is not None)
    assert(find_executable('npm') is not None)
    service = AppiumService()
    service.start()
    assert(service.is_running())
    service.stop()
    assert(not service.is_running())
