#!/bin/sh
set -eu

# The module reference lives alongside the authored guides. Sphinx generates
# individual options pages from the autosummary table in api.rst.
make html
