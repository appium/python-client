import os

SERVER_URL_BASE = f'http://{os.getenv("APPIUM_TEST_SERVER_HOST", "127.0.0.1")}:{os.getenv("APPIUM_TEST_SERVER_PORT", "4723")}'
