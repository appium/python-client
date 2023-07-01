# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from appium.options.base_options import OptionsDescriptor
from appium.options.transformers import DurationTransformer
from appium.options.common.supports_capabilities import SupportsCapabilities

class ArgumentsOption(SupportsCapabilities):
    ARGUMENTS = 'arguments'
    arguments = OptionsDescriptor('ARGUMENTS')
    """
    Gets and Sets the array of application command line arguments. This capability is
    only going to be applied if the application is not running on session startup.

    Usage
    -----
    - Get
        - `self.arguments`
    - Set
        - `self.arguments` = `value`
    
    Parameters
    ----------
    `value`: `List[str]`

    Returns
    -------
    - Get
        - `Optional[List[str]]`
    - Set
        - `None`
    """


class BootstrapRootOption(SupportsCapabilities):
    BOOTSTRAP_ROOT = 'bootstrapRoot'
    bootstrap_root = OptionsDescriptor('BOOTSTRAP_ROOT')
    """
    Gets and Sets the full path to WebDriverAgentMac root folder where Xcode project
    of the server sources lives. By default, this project is located in
    the same folder where the corresponding driver Node.js module lives.

    Usage
    -----
    - Get
        - `self.bootstrap_root`
    - Set
        - `self.bootstrap_root` = `value`
    
    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - `None`
    """


class EnvironmentOption(SupportsCapabilities):
    ENVIRONMENT = 'environment'
    environment = OptionsDescriptor('ENVIRONMENT')
    """
    Gets and Sets the dictionary of environment variables (name-&gt;value) that are going to be passed
    to the application under test on top of environment variables inherited from
    the parent process. This option is only going to be applied if the application
    is not running on session startup.

    Usage
    -----
    - Get
        - `self.environment`
    - Set
        - `self.environment` = `value`
    
    Parameters
    ----------
    `value`: `Dict[str, str]`

    Returns
    -------
    - Get
        - `Optional[Dict[str, str]]`
    - Set
        - `None`
    """


class ServerStartupTimeoutOption(SupportsCapabilities):
    SERVER_STARTUP_TIMEOUT = 'serverStartupTimeout'

    _transform_duration_get = DurationTransformer.transform_duration_get
    _transform_duration_set = DurationTransformer.transform_duration_set
    server_startup_timeout = OptionsDescriptor('SERVER_STARTUP_TIMEOUT', _transform_duration_get, _transform_duration_set)
    """
    Gets and Sets the timeout to wait util the WebDriverAgentMac
    project is built and started.

    Usage
    -----
    - Get
        - `self.server_startup_timeout`
    - Set
        - `self.server_startup_timeout` = `value`
    
    Parameters
    ----------
    `value`: `Union[int, timedelta]`

    Returns
    -------
    - Get
        - `Optional[timedelta]`
    - Set
        - `None`
    """


class ShowServerLogsOption(SupportsCapabilities):
    SHOW_SERVER_LOGS = 'showServerLogs'
    show_server_logs = OptionsDescriptor('SHOW_SERVER_LOGS')
    """
    Gets and Sets it to true in order to include xcodebuild output to the Appium
    server log. false by default.

    Usage
    -----
    - Get
        - `self.show_server_logs`
    - Set
        - `self.show_server_logs` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """


class WebDriverAgentMacUrlOption(SupportsCapabilities):
    WEB_DRIVER_ARGENT_MAC_URL = 'webDriverAgentMacUrl'
    web_driver_agent_mac_url = OptionsDescriptor('WEB_DRIVER_ARGENT_MAC_URL')
    """
    Gets and Sets the URL Appium will connect to an existing WebDriverAgentMac
    instance at this URL instead of starting a new one.

    Usage
    -----
    - Get
        - `self.web_driver_agent_mac_url`
    - Set
        - `self.web_driver_agent_mac_url` = `value`
    
    Parameters
    ----------
    `value`: `str`

    Returns
    -------
    - Get
        - `Optional[str]`
    - Set
        - `None`
    """


class SkipAppKillOption(SupportsCapabilities):
    SKIP_APP_KILL = 'skipAppKill'
    skip_app_kill = OptionsDescriptor('SKIP_APP_KILL')
    """
    Gets and Sets whether to skip the termination of the application under test
    when the testing session quits. false by default. This capability
    is only going to be applied if bundleId is set.

    Usage
    -----
    - Get
        - `self.skip_app_kill`
    - Set
        - `self.skip_app_kill` = `value`
    
    Parameters
    ----------
    `value`: `bool`

    Returns
    -------
    - Get
        - `Optional[bool]`
    - Set
        - `None`
    """