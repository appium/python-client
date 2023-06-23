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

from typing import Any, TypeVar

from appium.options.common.supports_capabilities import SupportsCapabilities

C = TypeVar("C", bound="SupportsCapabilities")


class SigningOptionsDescriptor:
    def __init__(self, name: str) -> None:
        self.name = name

    def __get__(self, obj: C, cls: type[C]) -> Any:
        return getattr(obj, "get_capability")(self.name)

    def __set__(self, obj: C, value: Any) -> Any:
        return getattr(obj, "set_capability")(self.name, value)


class KeyAliasOption(SupportsCapabilities):
    KEY_ALIAS = 'keyAlias'
    key_alias = SigningOptionsDescriptor("KEY_ALIAS")
    """
    The alias of the key in the keystore file provided in keystorePath capability.
    This option is used in combination with useKeystore, keystorePath,
    keystorePassword, keyAlias and keyPassword options. Unset by default

    Usage
    -----
    - `self.key_alias`
    - `self.key_alias` = `value`
    """


class KeyPasswordOption(SupportsCapabilities):
    KEY_PASSWORD = 'keyPassword'
    key_password = SigningOptionsDescriptor("KEY_PASSWORD")
    """
    The password of the key in the keystore file provided in keystorePath capability.
    This option is used in combination with useKeystore, keystorePath,
    keystorePassword, keyAlias and keyPassword options. Unset by default

    Usage
    -----
    - `self.key_password`
    - `self.key_password` = `value`
    """


class KeystorePasswordOption(SupportsCapabilities):
    KEYSTORE_PASSWORD = 'keystorePassword'
    keystore_password = SigningOptionsDescriptor("KEYSTORE_PASSWORD")
    """
    The password to the keystore file provided in keystorePath capability.
    This option is used in combination with useKeystore, keystorePath,
    keystorePassword, keyAlias and keyPassword options. Unset by default

    Usage
    -----
    - `self.keystore_password`
    - `self.keystore_password` = `value`
    """


class KeystorePathOption(SupportsCapabilities):
    KEYSTORE_PATH = 'keystorePath'
    keystore_path = SigningOptionsDescriptor("KEYSTORE_PATH")
    """
    The full path to the keystore file on the server filesystem.
    This option is used in combination with useKeystore, keystorePath,
    keystorePassword, keyAlias and keyPassword options. Unset by default

    Usage
    -----
    - `self.keystore_path`
    - `self.keystore_path` = `value`
    """


class NoSignOption(SupportsCapabilities):
    NO_SIGN = 'noSign'
    no_sign = SigningOptionsDescriptor("NO_SIGN")
    """
     Whether to use a custom keystore to sign the app under test.
    false by default, which means apps are always signed with the default A
    ppium debug certificate (unless canceled by noSign capability).
    This option is used in combination with keystorePath, keystorePassword,
    keyAlias and keyPassword options.

    Usage
    -----
    - `self.no_sign`
    - `self.no_sign` = `value`
    """

class UseKeystoreOption(SupportsCapabilities):
    USE_KEYSTORE = 'useKeystore'
    use_keystore = SigningOptionsDescriptor("USE_KEYSTORE")
    """
    Whether to use a custom keystore to sign the app under test.
    false by default, which means apps are always signed with the default A
    ppium debug certificate (unless canceled by noSign capability).
    This option is used in combination with keystorePath, keystorePassword,
    keyAlias and keyPassword options.

    Usage
    -----
    - `self.use_keystore`
    - `self.use_keystore` = `value`
    """