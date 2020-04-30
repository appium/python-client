#!/bin/sh
rm -rf *rst _build
sphinx-apidoc -F -H 'Appium python client' -o . ../appium/webdriver
make html
