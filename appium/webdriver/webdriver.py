#!/usr/bin/python

from selenium import webdriver

class WebDriver(webdriver.Remote):
    def __init__(self, command_executor='http://127.0.0.1:4444/wd/hub',
        desired_capabilities=None, browser_profile=None, proxy=None, keep_alive=False):

        # we have no new initialization to do
        super(WebDriver, self).__init__(command_executor, desired_capabilities, browser_profile, proxy, keep_alive)
