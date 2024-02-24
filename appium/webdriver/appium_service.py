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
import re
import subprocess as sp
import sys
import time
from typing import Any, List, Optional, Set

from selenium.webdriver.remote.remote_connection import urllib3

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 4723
STARTUP_TIMEOUT_MS = 60000
MAIN_SCRIPT_PATH = 'appium/build/lib/main.js'
STATUS_URL = '/status'
DEFAULT_BASE_PATH = '/'


class AppiumServiceError(RuntimeError):
    pass


class AppiumStartupError(RuntimeError):
    pass


def find_executable(executable: str) -> Optional[str]:
    path = os.environ['PATH']
    paths = path.split(os.pathsep)
    _, ext = os.path.splitext(executable)
    if sys.platform == 'win32' and not ext:
        executable = executable + '.exe'

    if os.path.isfile(executable):
        return executable

    for p in paths:
        full_path = os.path.join(p, executable)
        if os.path.isfile(full_path):
            return full_path

    return None


def get_node() -> str:
    result = find_executable('node')
    if result is None:
        raise AppiumServiceError(
            'NodeJS main executable cannot be found. Make sure it is installed and present in PATH'
        )
    return result


def get_npm() -> str:
    result = find_executable('npm.cmd' if sys.platform == 'win32' else 'npm')
    if result is None:
        raise AppiumServiceError(
            'Node Package Manager executable cannot be found. Make sure it is installed and present in PATH'
        )
    return result


def get_main_script(node: Optional[str], npm: Optional[str]) -> str:
    result: Optional[str] = None
    npm_path = npm or get_npm()
    for args in [['root', '-g'], ['root']]:
        try:
            modules_root = sp.check_output([npm_path] + args).strip().decode('utf-8')
            if os.path.exists(os.path.join(modules_root, MAIN_SCRIPT_PATH)):
                result = os.path.join(modules_root, MAIN_SCRIPT_PATH)
                break
        except sp.CalledProcessError:
            continue
    if result is None:
        node_path = node or get_node()
        try:
            result = (
                sp.check_output([node_path, '-e', f'console.log(require.resolve("{MAIN_SCRIPT_PATH}"))'])
                .decode('utf-8')
                .strip()
            )
        except sp.CalledProcessError as e:
            raise AppiumServiceError(e.output) from e
    return result


def parse_arg_value(args: List[str], arg_names: Set[str], default: str) -> str:
    for idx, arg in enumerate(args):
        if arg in arg_names and idx < len(args) - 1:
            return args[idx + 1]
    return default


def parse_port(args: List[str]) -> int:
    return int(parse_arg_value(args, {'--port', '-p'}, str(DEFAULT_PORT)))


def parse_base_path(args: List[str]) -> str:
    return parse_arg_value(args, {'--base-path', '-pa'}, DEFAULT_BASE_PATH)


def parse_host(args: List[str]) -> str:
    return parse_arg_value(args, {'--address', '-a'}, DEFAULT_HOST)


def make_status_url(args: List[str]) -> str:
    base_path = parse_base_path(args)
    return STATUS_URL if base_path == DEFAULT_BASE_PATH else f'{re.sub(r"/+$", "", base_path)}{STATUS_URL}'


class AppiumService:
    def __init__(self) -> None:
        self._process: Optional[sp.Popen] = None
        self._cmd: Optional[List[str]] = None

    def _poll_status(self, host: str, port: int, path: str, timeout_ms: int) -> bool:
        time_started_sec = time.time()
        conn = urllib3.PoolManager(timeout=1.0)
        while time.time() < time_started_sec + timeout_ms / 1000.0:
            if not self.is_running:
                raise AppiumStartupError()
            # noinspection PyUnresolvedReferences
            try:
                resp = conn.request('HEAD', f'http://{host}:{port}{path}')
                if resp.status < 400:
                    return True
            except urllib3.exceptions.HTTPError:
                pass
            time.sleep(1.0)
        return False

    def start(self, **kwargs: Any) -> sp.Popen:
        """Starts Appium service with given arguments.

        If you use the service to start Appium 1.x
        then consider providing ['--base-path', '/wd/hub'] arguments. By default,
        the service assumes Appium server listens on '/' path, which is the default path
        for Appium 2.

        The service will be forcefully restarted if it is already running.

        Keyword Args:
            env (dict): Environment variables mapping. The default system environment,
                which is inherited from the parent process, is assigned by default.
            node (str): The full path to the main NodeJS executable. The service will try
                to retrieve it automatically if not provided.
            npm (str): The full path to the Node Package Manager (npm) script. The service will try
                to retrieve it automatically if not provided.
            stdout (int): Check the documentation for subprocess.Popen for more details.
                The default value is subprocess.DEVNULL on Windows and subprocess.PIPE on other platforms.
            stderr (int): Check the documentation for subprocess.Popen for more details.
                The default value is subprocess.DEVNULL on Windows and subprocess.PIPE on other platforms.
            timeout_ms (int): The maximum time to wait until Appium process starts listening
                for HTTP connections. If set to zero or a negative number then no wait will be applied.
                60000 ms by default.
            main_script (str): The full path to the main Appium executable
                (usually located at build/lib/main.js). If not set
                then the service tries to detect the path automatically.
            args (str): List of Appium arguments (all must be strings). Check
                https://appium.io/docs/en/writing-running-appium/server-args/ for more details
                about possible arguments and their values.

        Returns:
            You can use Popen.communicate interface or stderr/stdout properties
            of the instance (stdout/stderr must not be set to None in such case) in order to retrieve the actual process
            output.
        """
        self.stop()

        env = kwargs['env'] if 'env' in kwargs else None
        node: str = kwargs.get('node') or get_node()
        npm: str = kwargs.get('npm') or get_npm()
        main_script: str = kwargs.get('main_script') or get_main_script(node, npm)
        # A workaround for https://github.com/appium/python-client/issues/534
        default_std = sp.DEVNULL if sys.platform == 'win32' else sp.PIPE
        stdout = kwargs['stdout'] if 'stdout' in kwargs else default_std
        stderr = kwargs['stderr'] if 'stderr' in kwargs else default_std
        timeout_ms = int(kwargs['timeout_ms']) if 'timeout_ms' in kwargs else STARTUP_TIMEOUT_MS
        args: List[str] = [node, main_script]
        if 'args' in kwargs:
            args.extend(kwargs['args'])
        self._cmd = args
        self._process = sp.Popen(args=args, stdout=stdout, stderr=stderr, env=env)
        error_msg: Optional[str] = None
        startup_failure_msg = (
            'Appium server process is unable to start. Make sure proper values have been '
            f'provided to \'node\' ({node}), \'npm\' ({npm}) and \'main_script\' ({main_script}) '
            f'method arguments.'
        )
        if timeout_ms > 0:
            status_url_path = make_status_url(args)
            try:
                if not self._poll_status(parse_host(args), parse_port(args), status_url_path, timeout_ms):
                    error_msg = (
                        f'Appium server has started but is not listening on {status_url_path} '
                        f'within {timeout_ms}ms timeout. Make sure proper values have been provided '
                        f'to --base-path, --address and --port process arguments.'
                    )
            except AppiumStartupError:
                error_msg = startup_failure_msg
        elif not self.is_running:
            error_msg = startup_failure_msg
        if error_msg is not None:
            if stderr == sp.PIPE and self._process.stderr is not None:
                err_output = self._process.stderr.read()
                if err_output:
                    error_msg += f'\nOriginal error: {str(err_output)}'
            self.stop()
            raise AppiumServiceError(error_msg)
        return self._process

    def stop(self) -> bool:
        """Stops Appium service if it is running.

        The call will be ignored if the service is not running
        or has been already stopped.

        Returns:
            `True` if the service was running before being stopped
        """
        is_terminated = False
        if self.is_running:
            assert self._process
            self._process.terminate()
            self._process.communicate(timeout=5)
            is_terminated = True
        self._process = None
        self._cmd = None
        return is_terminated

    @property
    def is_running(self) -> bool:
        """Check if the service is running.

        Returns:
            bool: `True` if the service is running
        """
        return self._process is not None and self._cmd is not None and self._process.poll() is None

    @property
    def is_listening(self) -> bool:
        """Check if the service is listening on the given/default host/port.

        The fact, that the service is running, does not always mean it is listening.
        The default host/port/base path values can be customized by providing
        --address/--port/--base-path command line arguments while starting the service.

        Returns:
            bool: `True` if the service is running and listening on the given/default host/port
        """
        if not self.is_running:
            return False

        assert self._cmd
        try:
            return self._poll_status(parse_host(self._cmd), parse_port(self._cmd), make_status_url(self._cmd), 1000)
        except AppiumStartupError:
            return False


if __name__ == '__main__':
    assert find_executable('node') is not None
    assert find_executable('npm') is not None
    service = AppiumService()
    service.start(args=['--address', '127.0.0.1', '-p', str(DEFAULT_PORT)])
    # service.start(args=['--address', '127.0.0.1', '-p', '80'], timeout_ms=2000)
    assert service.is_running
    assert service.is_listening
    service.stop()
    assert not service.is_running
    assert not service.is_listening
