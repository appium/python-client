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

import logging
import sys
from collections.abc import Iterator

import pytest

from appium.common.logger import logger, setup_logger


@pytest.fixture(autouse=True)
def restore_logger() -> Iterator[None]:
    # setup_logger mutates the shared module logger, so put it back after each test.
    handlers = list(logger.handlers)
    level = logger.level
    propagate = logger.propagate
    yield
    logger.handlers[:] = handlers
    logger.setLevel(level)
    logger.propagate = propagate


def test_setup_logger_default() -> None:
    handlers_before = list(logger.handlers)

    setup_logger()

    assert logger.propagate is False
    assert logger.level == logging.NOTSET
    assert len(logger.handlers) == len(handlers_before) + 1

    new_handler = logger.handlers[-1]
    assert isinstance(new_handler, logging.StreamHandler)
    assert new_handler.stream == sys.stderr


def test_setup_logger_custom_level() -> None:
    handlers_before = list(logger.handlers)

    setup_logger(level=logging.DEBUG)

    assert logger.propagate is False
    assert logger.level == logging.DEBUG
    assert len(logger.handlers) == len(handlers_before) + 1

    new_handler = logger.handlers[-1]
    assert isinstance(new_handler, logging.StreamHandler)
    assert new_handler.stream == sys.stderr
