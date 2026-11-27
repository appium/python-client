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

from appium.options.common.supports_capabilities import SupportsCapabilities

PERF_METRICS = 'perfMetrics'


class PerfMetricsOption(SupportsCapabilities):
    @property
    def perf_metrics(self) -> bool | None:
        """
        Whether per-session performance counters are enabled.
        """
        return self.get_capability(PERF_METRICS)

    @perf_metrics.setter
    def perf_metrics(self, value: bool) -> None:
        """
        Enable or disable per-session performance counters for driver calls.
        """
        self.set_capability(PERF_METRICS, value)
