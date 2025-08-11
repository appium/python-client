#!/bin/sh
rm -rf *rst _build
uv run sphinx-apidoc -F -H 'Appium python client' -o . ../appium/webdriver
make html
