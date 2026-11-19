import json
from datetime import timedelta
from pathlib import Path

import httpretty

from appium import webdriver
from appium.options.windows import WincoreOptions
from appium.options.windows.wincore import WincoreOptions as WincoreOptionsDirect
from test.helpers.constants import SERVER_URL_BASE


def test_wincore_default_capabilities():
    assert WincoreOptions is WincoreOptionsDirect
    options = WincoreOptions()

    assert options.platform_name == 'Windows'
    assert options.automation_name == 'Wincore'
    assert options.to_capabilities() == {
        'automationName': 'Wincore',
        'platformName': 'Windows',
    }
    assert options.to_w3c() == {
        'capabilities': {
            'firstMatch': [{}],
            'alwaysMatch': {
                'platformName': 'Windows',
                'appium:automationName': 'Wincore',
            },
        }
    }


def test_wincore_unset_properties_return_none():
    options = WincoreOptions()

    assert options.app is None
    assert options.app_top_level_window is None
    assert options.app_arguments is None
    assert options.app_working_dir is None
    assert options.prerun is None
    assert options.postrun is None
    assert options.wait_for_app_launch is None
    assert options.should_close_app is None
    assert options.force_quit is None
    assert options.isolated_script_execution is None
    assert options.smooth_pointer_move is None
    assert options.delay_before_click is None
    assert options.delay_after_click is None
    assert options.log_file is None
    assert options.perf_metrics is None
    assert options.webview_enabled is None
    assert options.webview_devtools_port is None
    assert options.chromedriver_executable_path is None
    assert options.edgedriver_executable_path is None
    assert options.chromedriver_cdn_url is None
    assert options.edgedriver_cdn_url is None
    assert options.ffmpeg_executable_path is None


def test_wincore_capabilities_roundtrip():
    options = WincoreOptions()
    options.app = r'C:\Windows\System32\notepad.exe'
    options.app_arguments = '/A test.txt'
    options.app_working_dir = r'C:\Temp'
    options.prerun = {'script': 'Write-Output "pre"'}
    options.postrun = {'command': 'Write-Output "post"'}
    options.should_close_app = False
    options.force_quit = True
    options.isolated_script_execution = True
    options.smooth_pointer_move = 'ease-in-out'
    options.delay_before_click = timedelta(seconds=1.15)
    options.delay_after_click = 75
    options.log_file = True
    options.perf_metrics = True
    options.webview_enabled = True
    options.webview_devtools_port = 9222
    options.chromedriver_executable_path = '/tools/chromedriver.exe'
    options.edgedriver_executable_path = '/tools/msedgedriver.exe'
    options.chromedriver_cdn_url = 'https://mirror.example/chromedriver'
    options.edgedriver_cdn_url = 'https://mirror.example/edgedriver'
    options.ffmpeg_executable_path = '/tools/ffmpeg.exe'

    assert options.app == r'C:\Windows\System32\notepad.exe'
    assert options.app_arguments == '/A test.txt'
    assert options.app_working_dir == r'C:\Temp'
    assert options.prerun == {'script': 'Write-Output "pre"'}
    assert options.postrun == {'command': 'Write-Output "post"'}
    assert options.should_close_app is False
    assert options.force_quit is True
    assert options.isolated_script_execution is True
    assert options.smooth_pointer_move == 'ease-in-out'
    assert options.delay_before_click == timedelta(milliseconds=1150)
    assert options.delay_after_click == timedelta(milliseconds=75)
    assert options.log_file is True
    assert options.perf_metrics is True
    assert options.webview_enabled is True
    assert options.webview_devtools_port == 9222
    assert options.chromedriver_executable_path == '/tools/chromedriver.exe'
    assert options.edgedriver_executable_path == '/tools/msedgedriver.exe'
    assert options.chromedriver_cdn_url == 'https://mirror.example/chromedriver'
    assert options.edgedriver_cdn_url == 'https://mirror.example/edgedriver'
    assert options.ffmpeg_executable_path == '/tools/ffmpeg.exe'

    w3c_caps = options.to_w3c()['capabilities']['alwaysMatch']
    assert w3c_caps == {
        'platformName': 'Windows',
        'appium:automationName': 'Wincore',
        'appium:app': r'C:\Windows\System32\notepad.exe',
        'appium:appArguments': '/A test.txt',
        'appium:appWorkingDir': r'C:\Temp',
        'appium:prerun': {'script': 'Write-Output "pre"'},
        'appium:postrun': {'command': 'Write-Output "post"'},
        'appium:shouldCloseApp': False,
        'ms:forcequit': True,
        'appium:isolatedScriptExecution': True,
        'appium:smoothPointerMove': 'ease-in-out',
        'appium:delayBeforeClick': 1150,
        'appium:delayAfterClick': 75,
        'appium:logFile': True,
        'appium:perfMetrics': True,
        'appium:webviewEnabled': True,
        'appium:webviewDevtoolsPort': 9222,
        'appium:chromedriverExecutablePath': '/tools/chromedriver.exe',
        'appium:edgedriverExecutablePath': '/tools/msedgedriver.exe',
        'appium:chromedriverCdnUrl': 'https://mirror.example/chromedriver',
        'appium:edgedriverCdnUrl': 'https://mirror.example/edgedriver',
        'appium:ffmpegExecutablePath': '/tools/ffmpeg.exe',
    }


def test_wincore_wait_for_app_launch_seconds_and_milliseconds():
    options = WincoreOptions()

    options.wait_for_app_launch = 10
    assert options.to_capabilities()['ms:waitForAppLaunch'] == 10
    assert options.wait_for_app_launch == timedelta(seconds=10)

    options.wait_for_app_launch = 120
    assert options.to_capabilities()['ms:waitForAppLaunch'] == 120
    assert options.wait_for_app_launch == timedelta(seconds=120)

    options.wait_for_app_launch = 5000
    assert options.to_capabilities()['ms:waitForAppLaunch'] == 5000
    assert options.wait_for_app_launch == timedelta(seconds=5)

    options.wait_for_app_launch = timedelta(seconds=15)
    assert options.to_capabilities()['ms:waitForAppLaunch'] == 15.0
    assert options.wait_for_app_launch == timedelta(seconds=15)

    options.wait_for_app_launch = timedelta(seconds=120)
    assert options.to_capabilities()['ms:waitForAppLaunch'] == 120.0
    assert options.wait_for_app_launch == timedelta(seconds=120)

    options.wait_for_app_launch = timedelta(seconds=150)
    assert options.to_capabilities()['ms:waitForAppLaunch'] == 150000
    assert options.wait_for_app_launch == timedelta(seconds=150)

    options.wait_for_app_launch = timedelta(seconds=120, milliseconds=500)
    assert options.to_capabilities()['ms:waitForAppLaunch'] == 120500
    assert options.wait_for_app_launch == timedelta(seconds=120, milliseconds=500)

    options.wait_for_app_launch = 0
    assert options.wait_for_app_launch == timedelta(0)


def test_wincore_zero_delays_and_pathlike_values():
    options = WincoreOptions()
    options.delay_before_click = 0
    options.delay_after_click = timedelta(0)
    options.log_file = False

    assert options.delay_before_click == timedelta(0)
    assert options.delay_after_click == timedelta(0)
    assert options.log_file is False

    log_path = Path('logs') / 'session.log'
    chrome_path = Path('drivers') / 'chromedriver.exe'
    edge_path = Path('drivers') / 'msedgedriver.exe'
    ffmpeg_path = Path('bin') / 'ffmpeg.exe'

    options.log_file = log_path
    options.chromedriver_executable_path = chrome_path
    options.edgedriver_executable_path = edge_path
    options.ffmpeg_executable_path = ffmpeg_path

    assert options.log_file == str(log_path)
    assert options.chromedriver_executable_path == str(chrome_path)
    assert options.edgedriver_executable_path == str(edge_path)
    assert options.ffmpeg_executable_path == str(ffmpeg_path)


def test_wincore_load_and_unset_capabilities():
    options = WincoreOptions().load_capabilities(
        {
            'appTopLevelWindow': '0x001A0B2C',
            'shouldCloseApp': False,
            'ms:forcequit': True,
            'ms:waitForAppLaunch': 2500,
            'appium:delayBeforeClick': 120,
            'appium:delayAfterClick': 50,
            'appium:webviewDevtoolsPort': 9333,
        }
    )

    assert options.app_top_level_window == '0x001A0B2C'
    assert options.should_close_app is False
    assert options.force_quit is True
    assert options.wait_for_app_launch == timedelta(milliseconds=2500)
    assert options.delay_before_click == timedelta(milliseconds=120)
    assert options.delay_after_click == timedelta(milliseconds=50)
    assert options.webview_devtools_port == 9333

    options.set_capability('ms:forcequit', None)
    options.set_capability('delayBeforeClick', None)
    assert options.force_quit is None
    assert options.delay_before_click is None


@httpretty.activate
def test_wincore_create_session_request_payload():
    options = WincoreOptions()
    options.app = 'Root'
    options.should_close_app = False
    options.force_quit = True
    options.wait_for_app_launch = timedelta(seconds=30)
    options.delay_before_click = timedelta(milliseconds=200)
    options.webview_enabled = True

    httpretty.register_uri(
        httpretty.POST,
        f'{SERVER_URL_BASE}/session',
        body=json.dumps({'value': {'sessionId': 'wincore-session', 'capabilities': {}}}),
    )

    driver = webdriver.Remote(SERVER_URL_BASE, options=options)
    assert driver.session_id == 'wincore-session'

    request_json = json.loads(httpretty.last_request().body.decode('utf-8'))
    assert request_json == {
        'capabilities': {
            'firstMatch': [{}],
            'alwaysMatch': {
                'platformName': 'Windows',
                'appium:automationName': 'Wincore',
                'appium:app': 'Root',
                'appium:shouldCloseApp': False,
                'ms:forcequit': True,
                'ms:waitForAppLaunch': 30.0,
                'appium:delayBeforeClick': 200,
                'appium:webviewEnabled': True,
            },
        }
    }
