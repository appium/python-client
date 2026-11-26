from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from test.helpers.constants import SERVER_URL_BASE


def test_find_character_map_font_selector():
    options = AppiumOptions().load_capabilities(
        {'platformName': 'windows', 'appium:automationName': 'Wincore', 'appium:app': r'%SystemRoot%\System32\charmap.exe'}
    )
    with webdriver.Remote(SERVER_URL_BASE, options=options) as driver:
        driver.implicitly_wait(10)
        font_selector = driver.find_element(
            AppiumBy.WINDOWS_UI_AUTOMATION, "new PropertyCondition(AutomationElement.AutomationIdProperty, '105')"
        )
        assert font_selector.get_attribute('AutomationId') == '105'
