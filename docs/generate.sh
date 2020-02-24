#!/bin/sh
sphinx-apidoc -F -o . ../appium/webdriver
make html
