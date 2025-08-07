#!/usr/bin/env bash

set -e
set -o pipefail

CONFIGURE_DIR=$(dirname "$0")
uv run python "${CONFIGURE_DIR}/script/release.py" "$@"

echo "Finish release process"
