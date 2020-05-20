#!/usr/bin/env bash

set -e
set -o pipefail

if [ -z "$PYTHON_BIN_PATH" ]; then
  PYTHON_BIN_PATH=$(which python3 || which python || true)
fi

export PYTHON_BIN_PATH

CONFIGURE_DIR=$(dirname "$0")
"$PYTHON_BIN_PATH" "${CONFIGURE_DIR}/script/release.py" "$@"

echo "Finish release process"
