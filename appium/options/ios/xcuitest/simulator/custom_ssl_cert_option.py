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

from typing import Optional

from appium.options.common.supports_capabilities import SupportsCapabilities

CUSTOM_SSL_CERT = 'customSSLCert'


class CustomSslCertOption(SupportsCapabilities):
    @property
    def custom_ssl_cert(self) -> Optional[str]:
        """
        SSL certificate content.
        """
        return self.get_capability(CUSTOM_SSL_CERT)

    @custom_ssl_cert.setter
    def custom_ssl_cert(self, value: str) -> None:
        """
        Adds a root SSL certificate to IOS Simulator.
        The certificate content must be provided in PEM format.
        """
        self.set_capability(CUSTOM_SSL_CERT, value)
