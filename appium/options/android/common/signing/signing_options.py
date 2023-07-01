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

from appium.options.transformers import OptionsDescriptor
from appium.options.common.supports_capabilities import SupportsCapabilities


class KeyAliasOption(SupportsCapabilities):
    KEY_ALIAS = 'keyAlias'
    key_alias = OptionsDescriptor('KEY_ALIAS')
    """
    The alias of the key in the keystore file provided in keystorePath capability.
    This option is used in combination with useKeystore, keystorePath,
    keystorePassword, keyAlias and keyPassword options. Unset by default

    Usage
    -----
    - Get
        - `self.key_alias`
    - Set
        - `self.key_alias` = `value`
    
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


class KeyPasswordOption(SupportsCapabilities):
    KEY_PASSWORD = 'keyPassword'
    key_password = OptionsDescriptor('KEY_PASSWORD')
    """
    The password of the key in the keystore file provided in keystorePath capability.
    This option is used in combination with useKeystore, keystorePath,
    keystorePassword, keyAlias and keyPassword options. Unset by default

    Usage
    -----
    - Get
        - `self.key_password`
    - Set
        - `self.key_password` = `value`
    
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


class KeystorePasswordOption(SupportsCapabilities):
    KEYSTORE_PASSWORD = 'keystorePassword'
    keystore_password = OptionsDescriptor('KEYSTORE_PASSWORD')
    """
    The password to the keystore file provided in keystorePath capability.
    This option is used in combination with useKeystore, keystorePath,
    keystorePassword, keyAlias and keyPassword options. Unset by default

    Usage
    -----
    - Get
        - `self.keystore_password`
    - Set
        - `self.keystore_password` = `value`
    
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


class KeystorePathOption(SupportsCapabilities):
    KEYSTORE_PATH = 'keystorePath'
    keystore_path = OptionsDescriptor('KEYSTORE_PATH')
    """
    The full path to the keystore file on the server filesystem.
    This option is used in combination with useKeystore, keystorePath,
    keystorePassword, keyAlias and keyPassword options. Unset by default

    Usage
    -----
    - Get
        - `self.keystore_path`
    - Set
        - `self.keystore_path` = `value`
    
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


class NoSignOption(SupportsCapabilities):
    NO_SIGN = 'noSign'
    no_sign = OptionsDescriptor('NO_SIGN')
    """
     Whether to use a custom keystore to sign the app under test.
    false by default, which means apps are always signed with the default A
    ppium debug certificate (unless canceled by noSign capability).
    This option is used in combination with keystorePath, keystorePassword,
    keyAlias and keyPassword options.

    Usage
    -----
    - Get
        - `self.no_sign`
    - Set
        - `self.no_sign` = `value`
    
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

class UseKeystoreOption(SupportsCapabilities):
    USE_KEYSTORE = 'useKeystore'
    use_keystore = OptionsDescriptor('USE_KEYSTORE')
    """
    Whether to use a custom keystore to sign the app under test.
    false by default, which means apps are always signed with the default A
    ppium debug certificate (unless canceled by noSign capability).
    This option is used in combination with keystorePath, keystorePassword,
    keyAlias and keyPassword options.

    Usage
    -----
    - Get
        - `self.use_keystore`
    - Set
        - `self.use_keystore` = `value`
    
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