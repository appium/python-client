Changelog
=========


v0.46 (2019-06-27)
------------------
- Bump 0.46. [Kazuaki Matsuo]
- Bug fix joining path in _get_main_script (#408) [Nicholas Frederick]
- Update changelog for 0.45. [Kazuaki Matsuo]


v0.45 (2019-06-26)
------------------
- Bump 0.45. [Kazuaki Matsuo]
- Add execute driver (#406) [Kazuaki Matsuo]

  * add execute driver

  * append docstring
- Add how to solve pipenv error to readme (#403) [Mori Atsushi]

  * Add how to solve pipenv error to readme

  * review comments

  * tweak

  * review comments
- Add autocompletion for pycharm (#404) [Mori Atsushi]

  * Add autocompletion for pycharm

  * Removed flaky tests from running
- Moving reset method from WebDriver to Applications (#399) [Mayura]
- Add unit test for open_notifications (#398) [tabatask]
- Run android functional tests on ci (#396) [Mori Atsushi]

  * Add android functional test to ci

  * Add missing param

  * Add run_test template

  * Fixed: test running failed

  * Fixed

  * Fixed

  * fixed

  * Add run_android_test

  * Changed emulator to Nexus6

  * Run all android tests

  * fixed

  * Resolve python-dateutil dependency

  * Run on 3 workers

  * Add chromedriver installation

  * Skip failed test cases on ci

  * fixed

  * Extend adbExecTimeout

  * Add script source to comment

  * Run 5 workers for android

  * Use Node11

  * Extend wait time

  * Reduced running android functional tests

  * Revert some changes
- Use the same format for docstring (#395) [Mori Atsushi]

  * Update docstring

  * Update docstring

  * Update docstring

  * tweak

  * tweak

  * tweak

  * tweak

  * tweak

  * Update docstring

  * Update docstring

  * Update docstring

  * Update docstring

  * tweak

  * Update
- Publish functional test report (#394) [Mori Atsushi]

  * Move functional tests to template

  * Add publish_test_result

  * Fix typo
- Divide functional appium tests into each module(iOS) (#391) [Mori
  Atsushi]

  * Divide ios appium_tests to each module

  * Fix test file name

  * Add CI status badge
- Run iOS functional tests on azure pipelines (#390) [Mori Atsushi]

  * Set up CI with Azure Pipelines

  * review comments

  * update README
- Update changelog for 0.44. [Kazuaki Matsuo]


v0.44 (2019-05-24)
------------------

Fix
~~~
- Installed selenium4 when 'setup.py install' (#389) [Mori Atsushi]

  * Fix: installed selenium4 when setup.py install

  * Keep existing comparison operator

Other
~~~~~
- Bump 0.44. [Kazuaki Matsuo]
- Support get_display_density (#388) [Mori Atsushi]

  * Support get_display_density

  * Add get_display_density unittest

  * Add api doc

  * Add return description to api doc
- Fix ios functional tests failed (#385) [Mori Atsushi]

  * Fix safari test(iOS)

  * Fix: find_by_ios_predicate

  * Delete find_by_uiautomation_tests

  since uiautomation is deprecated

  * Move non test files

  * Replace test app with the latest

  * Fix tests failed along to replaced test app

  * review comments
- Support set_network_speed (#386) [Mori Atsushi]

  * Support set_nework_speed

  * Add set_network_speed unittest

  * Add api doc

  * revert unexpected change

  * revert change
- Update changelog for 0.43. [Kazuaki Matsuo]


v0.43 (2019-05-18)
------------------
- Bump 0.43. [Kazuaki Matsuo]
- Add assertions for w3c (#384) [Kazuaki Matsuo]
- Add isort to pre-commit (#379) [Mori Atsushi]

  * Add isort to pre-commit

  * Add isort.conf

  * Applied isort for test/unit

  * Add current dir to isrot arg

  * Add check to ci.sh

  * Use exit code for condition check in ci.sh
- [RD-34891] Assign w3c property on the command executor. (#382)
  [Erustus Agutu]
- Get rid of sessionId (#383) [Kazuaki Matsuo]
- Divide functional appium tests into each module(android) (#378) [Mori
  Atsushi]

  * Move non test files

  * Divide appium_tests into each module tests(android)

  * Skip contexts, find_by_image tests

  * Removed unnecessary codes
- Introduced pipfile (#376) [Mori Atsushi]

  * Added Pipfile

  Just created by pipenv install -r ci-requirements.txt

  * Introduced pipenv

  * Add Pipfile.lock to gitignore

  * Cover any minor versions for packages
- Fix functional tests failed (android, push_file)  (#375) [Mori
  Atsushi]

  * Fix: test_push_file

  * Move remove_fs tests

  * Move teardown process

  * Delete selendroid test

  * tweak

  * Update along to review comments

  * Replace double quote with single quote under android dir

  * Remove creating tmp file

  * tweak
- Fix functional tests failed (android, ime/multi_action) (#372) [Mori
  Atsushi]

  * Fix test failed: ime_tests, multi_action_tests

  * revert change and add impl for python3

  * Remove py3 dependency

  * Change deepcopy to copy

  * Update ime_tests
- Fix functional tests failed (android, touch_action) (#374) [Mori
  Atsushi]

  * Fix: test_drag_and_drop

  * Fix: test_long_press

  * Fix: long_press_x_y, swipe

  * Fix: press_and_wait

  * Fix: driver_drag_and_drop

  * Tweak

  * Add SLEEPY_TIME

  * Remove set with sleep and find_element
- Move android commands to android package (#371) [Mori Atsushi]

  * Reorder mobilecommands

  * Move android commands to android package

  * Update setup.py to include added packages

  * Changed find_packages to whitelist style
- Update changelog for 0.42. [Kazuaki Matsuo]


v0.42 (2019-05-10)
------------------
- Bump 0.42. [Kazuaki Matsuo]
- Fix functional tests failed (android, appium_tests) (#366) [Mori
  Atsushi]

  * Fix test failed: test_send_keys, test_screen_record

  * Fix test failed: test_update_settings

  * Fix test failed: test_start_activity_other_app

  * Move and rename helper package

  * Update along to review comments

  * Add return value to wait_for_element
- Support get_performance_data, get_performance_data_types (#368) [Mori
  Atsushi]

  * Support get_performance_data, get_performance_data_types

  * Add api doc

  * Add performance unittest

  * Tweak

  * Update api doc
- Fix poll_url in Python 3 (#370) [Kazuaki Matsuo]
- Support set_gsm_voice (#367) [Mori Atsushi]

  * Support set_gsm_voice

  * Add set_gsm_voice unittest

  * Fix typo
- Fix functional tests failed (#364) [Mori Atsushi]

  * Fix test failed: element_location_in_view, set_text

  * Fix test failed: test_push_file

  * Merge test_pull_test into test_push_test

  * Fix test failed: test_pull_folder

  * Enable running by both py2 and py3

  * Removed unnecessary codes

  * Remove magic number
- Support get_system_bars (#363) [Mori Atsushi]

  * Support get_system_bars

  * Add api doc

  * Add get_system_bars unittest

  * Remove FIXME
- Support make_gsm_call (#360) [Mori Atsushi]

  * Move const to gsm_signal_strength

  * Support make_gsm_call

  * Add make_gsm_call unittest

  * Move const to gsm class

  * Move get_dict_const to common.helper

  * Rename func

  * Use OrderedDict to keep defined order
- Support set_gsm_signal (#357) [Mori Atsushi]

  * Support set_gsm_signal

  * Fix: NONE_OR_UNKNOWN doesn't work

  * Add set_gsm_signal unittest

  * Use int for signal strength const

  * Raise exception when signal strength is out of range

  * Fix: wrong class name

  * Removed args validation

  Since arg validation already done by server side

  * Show warning log when arg is out of range

  * Some changes for less maintenance
- Mobile:pinchOpen and mobile:pinchClose no longer implemented in appium
  drivers (#358) [Jonah]
- Remove unnecessary codes. [Atsushi Mori]
- Replace 'on' with AC_ON. [Atsushi Mori]
- Update api doc. [Atsushi Mori]
- Define AC_OFF, AC_ON as const. [Atsushi Mori]
- Skip pylint warnings. [Atsushi Mori]
- Add return value. [Atsushi Mori]
- Update api doc. [Atsushi Mori]
- Add set_power_ac unittest. [Atsushi Mori]
- Support set_power_ac. [Atsushi Mori]
- Added set_power_capacity unittest. [Atsushi Mori]
- Support set_power_capacity. [Atsushi Mori]
- Update changelog for 0.41. [Kazuaki Matsuo]
- Bump 0.41. [Kazuaki Matsuo]


v0.41 (2019-04-23)
------------------
- Fix True/False in image settings, add boolean value in settings test
  (#352) [Kazuaki Matsuo]

  * Fix True/False in image settings, add boolean value in settings test

  * use is for boolean
- Add send sms support (#351) [Mori Atsushi]

  * Support sendSms function

  * Added api doc

  * Add sms unittest

  * Revert unexpected changes

  * Update api doc
- Make keep alive True by default (#348) [Kazuaki Matsuo]
- Move settings to mixin classes (#347) [Mori Atsushi]
- Add pixelFormat in docstring (#346) [Kazuaki Matsuo]
- Add fingerprint unittest (#345) [Mori Atsushi]
- Add shake unittest (#344) [Mori Atsushi]
- Update changelog for 0.40. [Kazuaki Matsuo]


v0.40 (2019-03-14)
------------------
- Bump 0.40. [Kazuaki Matsuo]
- Update missing changelog in 0.39. [Kazuaki Matsuo]
- Fix RuntimeError: maximum recursion depth exceeded in cmp happened
  (#343) [Kazuaki Matsuo]

  * fix maximum recursion depth exceeded in sub classes

  * add docstring

  * add comparison of a number of commands

  * use issubclass to ensure the class is sub


v0.39 (2019-02-27)
------------------
- Add direct connect flag to be able to handle directConnectXxxxc (#338)
  [Kazuaki Matsuo]

  * add direct connect feature

  * rmeove todo

  * update readme, extract _update_command_executor

  * add logger

  * make log level info

  * show warning if no directConnectXxxxx in dict

  * tweak error message

  * tweak message format
- Add datamatcher (#335) [Kazuaki Matsuo]

  * add datamatcher

  * add zero case

  * defines search context for driver and element
- Update changelog for 0.38. [Kazuaki Matsuo]
- Bump 0.38. [Kazuaki Matsuo]


v0.38 (2019-02-11)
------------------
- Bump 0.38. [Kazuaki Matsuo]
- Remove io.open from getting version code (#334) [Kazuaki Matsuo]

  * remove io.open

  * remove appium module from release script


v0.37 (2019-02-10)
------------------
- Cast set_location arguments to float (#332) [Mykola Mokhnach]
- Fix passing options to screen record commands (#330) [Mykola Mokhnach]
- Add AppiumConnection to customise user agent (#327) [Kazuaki Matsuo]
- Add a test for reset (#326) [Kazuaki Matsuo]
- Add a simple class to control Appium execution from the client code
  (#324) [Mykola Mokhnach]
- Add pressure option (#322) [Kazuaki Matsuo]

  * add pressure option

  * add a test, tweak comment and the method

  * fix typo
- Add a test case using another session id (#320) [Kazuaki Matsuo]
- Update changelog for 0.36. [Kazuaki MATSUO]
- Bump 0.36. [Kazuaki MATSUO]


v0.36 (2019-01-18)
------------------
- Bump 0.36. [Kazuaki MATSUO]
- Import keyboard, add tests (#319) [Kazuaki Matsuo]
- Update changelog for 0.35. [Kazuaki MATSUO]


v0.35 (2019-01-17)
------------------
- Bump 0.35. [Kazuaki MATSUO]
- Add location unittest (#317) [Mori Atsushi]

  * Add test_location

  * Add test_set_location

  * Add test_toggle_location_services
- Add settings unittest (#315) [Mori Atsushi]

  * Add settings unittest

  * Remove unused import
- Move device_time to a mixin class (#314) [Mori Atsushi]
- Define getting httpretty request body decoded by utf-8 (#313) [Kazuaki
  Matsuo]

  * define httpretty_last_request_body

  * replace the order

  * update

  * rename
- Added format to device_time as argument (#312) [Mori Atsushi]
- Add devicetime unittest (#309) [Mori Atsushi]

  * Add device time test

  * Removed unnecessary check from device time test

  * Changed assertion for device time test

  Along to review comments

  * Changed quote for string from double to single
- Add activities unittest (#310) [Tadashi Nemoto]

  * Add test_start_activity

  * Add current_activity and wait_activity

  * Fix pytest 4.0.2

  * Add test_start_activity_with_opts

  * Added options
- Add network unittest (#308) [Mori Atsushi]

  * Add network connection test

  * Added set network connection test

  * Add toggle wifi test

  * Removed unnecessary codes from toggle wifi test

  * Changed assertion for set network connection test
- Add touch action unittest (#306) [Tadashi Nemoto]

  * Add press test

  * Add test_long_press

  * Add test_wait

  * Add remaining tests

  * Add tap

  * 10 -> 9

  * Modify  based on comment
- Move action and keyboard helpers to mixin classes (#307) [Mykola
  Mokhnach]
- Add precommit (#304) [Kazuaki Matsuo]

  * add pre-commit hook
- Fixing broken pypi long description rendering (#303) [Prabhash]

  reference: https://packaging.python.org/guides/making-a-pypi-friendly-readme

  Tested at https://pypi.org/project/delayed-assert
- Extract more webdriver methods into specialized mixin classes (#302)
  [Mykola Mokhnach]
- Move specialized method groups to mixin classes (#301) [Mykola
  Mokhnach]
- Fix overridden mixin method call (#297) [Mykola Mokhnach]
- Update changelog for 0.34. [Kazuaki MATSUO]


v0.34 (2018-12-18)
------------------
- Bump 0.34. [Kazuaki MATSUO]
- Fix missing package, missing commands and a test (#296) [Kazuaki
  Matsuo]

  * add extensions into package

  * add tests for context to make sure it loads

  * move command definition from extensions to root
- Update changelog for 0.33. [Kazuaki MATSUO]


v0.33 (2018-12-18)
------------------
- Bump 0.33. [Kazuaki MATSUO]
- Move read version (#294) [Kazuaki Matsuo]
- Add newline in release script because of autopep8 (#292) [Kazuaki
  Matsuo]
- Update changelog for 0.32. [Kazuaki MATSUO]


v0.32 (2018-12-18)
------------------
- Bump 0.32. [Kazuaki MATSUO]
- Split driver methods into mixin classes (#291) [Mykola Mokhnach]
- Run with tox on travis (#290) [Kazuaki Matsuo]

  * run with tox on travis

  * update readme
- Add unit tests for isLocked Library (#288) [Venkatesh Singh]

  * Add unit tests for isLocked Lib

  * moved isLocked library tests in lock.py
- Add unit test for lock lib (#287) [Venkatesh Singh]

  * Add unit test for lock lib
- Improve pytest, adding pytest.ini and set default arguments (#284)
  [Kazuaki Matsuo]
- Extract bytes and add a test for set clipboard (#282) [Kazuaki Matsuo]

  * extract bytes and add a test for set clipboard
- Introduce httpretty for unittest to mock Appium server (#281) [Kazuaki
  Matsuo]

  * add httpretty

  * add clipboard tests as an example

  * add test for forceMjsonwp
- Update setup elements (#280) [Kazuaki Matsuo]

  * update setup elements

  * remove docgen since we can use markdown format in pypi
- Release automation (#276) [Kazuaki Matsuo]
- Fixed few failing tests in appium_tests.py (#278)
  [RajeshkumarAyyadurai]

  * fixed few failing tests in appium_tests.py

  * updated few tests in appium_tests.py by removing uiautomator strategy
- Fixed failing tests in find_by_accessibility_id_tests.py.
  [RajeshkumarAyyadurai]
- Updated requirements.txt file with version (#275)
  [RajeshkumarAyyadurai]

  * updated required dependecies with version number as a best practice

  * updated required dependencies with version

  * updated pylint library version to support for python 2.7
- Append document for recording screen (#271) [Kazuaki Matsuo]

  * append document for recording screen

  * add since appium 1.10.0

  * remove Only works for real devices since the feature can work on both
- Update changelog for 0.31. [Kazuaki MATSUO]


v0.31 (2018-11-21)
------------------
- V0.31. [Kazuaki MATSUO]
- Driver.push_file(destination_path, source_path) feature (#270) [Javon
  Davis]

  * used base64 library for conversion

  * remove unnecessary library use

  * changed text in test file

  * * Using context when reading file
  * changed docstring format
  * Catch error thrown if file not present and present user with a better message

  * fixed incorrect file path in test

  * removed change in pul_file that broke backwards compat and updated docstring description for `destination_path`


v0.30 (2018-10-31)
------------------
- V0.30. [Kazuaki MATSUO]
- Fix python3 set_clipboard error (#267) [Kazuaki Matsuo]

  * fix python3 set_clipboard error

  * apply formatter
- Add release section in readme. [Kazuaki MATSUO]


v0.29 (2018-10-30)
------------------
- V0.29. [Kazuaki MATSUO]
- Add an endpoint for pressing buttons (#262) [Alex]
- Add custom locator strategy (#260) [Jonathan Lipps]
- Bump selenium 3.14.1, call RemoteCommand without workaround (#259)
  [Kazuaki Matsuo]

  * bump selenium 3.14.1, call RemoteCommand without workaround

  * make attributeValue check safe

  * define str = basestring for Python 2

  * apply formatter

  * add missing value check
- Add a duration for scroll for ios (#256) [Kazuaki Matsuo]

  * add a duration for scroll for ios

  * tweak default duration

  * apply autoformat

  * set 600 duration by default if it's w3c spec

  * skip wait if duration is none

  * add comment
- Update obsolete link for mobile json wire protocol spec. (#257)
  [Andrei Petre]
- Add finger print (#252) [Kazuaki Matsuo]

  * add fingre print

  * apply auto format
- Add find_elements w3c for webelement (#251) [Kazuaki Matsuo]

  * add find_elements w3c for webelement

  * add tests for child elements

  * add todo for future work
- Add a github issue template (#250) [Kazuaki Matsuo]
- Add xdist port handling (#248) [Kazuaki Matsuo]

  * add handling port number to run ios tests in parallel

  * define PytestXdistWorker

  * use gw0 if the number of worker is over the count of workers
- Remove always_match and use first_match instead (#246) [Kazuaki
  Matsuo]

  remove always_match and use first_match instead
- Use normal element for find image by (#236) [Kazuaki Matsuo]

  * use normal element

  * get rid of png

  * get rid of imagelement.py

  * apply formatter
- Typo fix: finiding -> finding (#245) [Andrew Fuller]
- Add autopep8 (#243) [Kazuaki Matsuo]

  * apply autopep8

  * add development section as the first draft

  * relax max-line-length

  * add global-config
- Add toggle wifi command (#241) [joshuazhusince1986]

  * add toggle_wifi command

  * update comment to indicate toggle_wifi is only for Android
- Add selenium into ci-requirements (#240) [Kazuaki Matsuo]

  fix pylint

  add --py3k
- Add travis to run pylint and unit tests (#239) [Kazuaki Matsuo]

  * add pylint

  * add rcfile

  * tweak pylint

  * fix lint

  * add running pytest

  * tweak indentations
- Add tag view for android (#238) [Kazuaki Matsuo]

  * add tag view for android

  * fix typo... and tweak names of arguments

  * tweak docstring

  * add find element by viewtag section in readme
- Tweak PyPi URLs and add a badge (#232) [Kazuaki Matsuo]


v0.28 (2018-07-13)
------------------
- V0.28. [Isaac Murchie]
- Fix base64 encoded string (#231) [Kazuaki Matsuo]


v0.27 (2018-07-10)
------------------
- V0.27. [Isaac Murchie]
- Set None as default value to lock device (#227) [Miguel Hernández]

  * Set 0 as default value to lock device

  * Set None as default value instead of 0
- Add support for is keyboard shown command. [Jonathan Lipps]
- Add find by image commands and tests (#224) [Jonathan Lipps]

  * add find by image commands and tests

  * remove and ignore pytest cache files

  * address review comments

  * fix docstrings
- Add flags argument to press_keycode (#222) [Mykola Mokhnach]

  * Add flags argument to press_keycode

  * Add flags to long press as well
- Add an endpoint for getting battery info (#217) [Mykola Mokhnach]
- Add wrappers for OpenCV-based image comparison (#216) [Mykola
  Mokhnach]

  * Add wrappers for OpenCV-based image comparison

  * Tune some docs
- Avoid setting coordinates to null for touch actions (#214) [Mykola
  Mokhnach]
- Add clipboard handlers (#209) [Mykola Mokhnach]

  * Add clipboard handlers

  * Fix documentation

  * fix options notation
- Change QUERY_APP_STATE request type to POST (#205) [Mykola Mokhnach]
- Add applications management endpoint handlers (#204) [Mykola Mokhnach]
- Add methods for start/stop screen record API endpoints (#201) [Mykola
  Mokhnach]

  * Add methods for start/stop screen record API endpoints

  * Fix typo

  * Add a separate test for Android and get rid of redundant stuff

  * Tune documentation

  * Add videoSize arg description

  * Fix arg name
- Add appium prefix in create session and fix find_elements for W3C
  (#196) [Kazuaki Matsuo]

  * add appium prefix in create session

  * fix find_elements by w3c for Appium

  * introduce forceMjsonwp

  * refine a bit

  * fix some tests

  * update the docset
- Add endpoints for lock/unlock. [Mykola Mokhnach]


v0.26 (2018-01-09)
------------------
- V0.26. [Isaac Murchie]


v0.25 (2018-01-09)
------------------
- V0.25. [Isaac Murchie]
- Only if key_name, key, and strategy are None do we need to set the
  strategy to 'tapOutside'. This change allows setting just the strategy
  to some other value, like 'swipeDown'. (#181) [Daniel Freer]
- Fix typos in the README. [Mel Shafer]
- Correct a wording. [Kazuaki MATSUO]
- Add method for getting current package. [Isaac Murchie]
- Create README.md. [Kazuaki Matsuo]
- Append class chain related descriptions. [Kazuaki MATSUO]
- Add tests for ios class chain and rename methods a bit. [Kazuaki
  MATSUO]
- Add class chain. [Kazuaki MATSUO]
- Add toggleTouchIdEnrollment. [Dan Graham]
- Update README to include instructions for using iOS predicates. [Emil
  Petersen]
- Update docs for UIAutomation selector to include version requirement.
  [Emil Petersen]


v0.24 (2016-12-20)
------------------
- V0.24. [Isaac Murchie]
- DontStopAppOnReset instead of stopAppOnReset. [s.zubov]
- Added test cases for clear and find elements by ios predicate string.
  [ben.zhou]
- Added clear to driver. Added find elements by ios predicate string.
  [ben.zhou]


v0.23 (2016-11-10)
------------------
- V0.23. [Isaac Murchie]
- Added touchId to driver (#143) [Dan Graham]

  * Added touchId to driver

  Wrote a test for it (still need help running Python tests though). Updated capabilities to use iOS 10.1


v0.22 (2016-03-16)
------------------
- V0.22. [Isaac Murchie]
- Use id instead of elementId. [Isaac Murchie]


v0.21 (2016-01-20)
------------------
- V0.21. [Isaac Murchie]
- Add device_time property. [Isaac Murchie]
- Fix saucetestcase to run under Python3. [Ling Lin]

  The module 'new' was removed. Instead of new.newclass, use type().
- Update README.md. [tophercf]

  smallest win in history


v0.20 (2015-10-12)
------------------
- V0.20. [Isaac Murchie]
- Revert actions change. [Isaac Murchie]


v0.19 (2015-10-09)
------------------
- V0.19. [Isaac Murchie]
- Change 'actions' to 'gestures' in single action. [Isaac Murchie]


v0.18 (2015-10-07)
------------------
- V0.18. [Isaac Murchie]
- Remove dependency on enum. [Isaac Murchie]
- Fixed typographical error, changed accomodate to accommodate in
  README. [orthographic-pedant]
- Bump version. [Isaac Murchie]
- Add string file argument to driver.app_strings. [Isaac Murchie]
- Use WebDriverWait to implement wait_activity. [zhaoqifa]
- Add wait_activity method for webdriver. [zhaoqifa]
- Make tap duration be handled as ms, not s. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Fix bug with monkeypatching. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Move monkeypatched set_value into WebElement. [Isaac Murchie]
- Add el.location_in_view method. [Isaac Murchie]
- Fix to issue #71. [James Salt]
- Fix start_activity for Python 3.x. [Artur Tanistra]
- Fix start_activity for Python3. [Isaac Murchie]


v0.14 (2015-03-06)
------------------
- Bump version. [Isaac Murchie]
- Fix issue with single tap. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Fix handling of sauce test case so ImportError is suppressed. [Isaac
  Murchie]


v0.12 (2015-01-13)
------------------
- Bump version. [Isaac Murchie]
- Add base class for Sauce tests. [Isaac Murchie]
- Add remaining optional arguments to start_activity method. [Isaac
  Murchie]
- Fix package names for starting activity. [Isaac Murchie]
- Update README.md. [Mikhail Martin]

  Missing dot causes errors.
- Update webdriver.py. [urtow]


v0.11 (2014-11-14)
------------------
- Bump version. [Isaac Murchie]
- Add toggle_location_services. [Isaac Murchie]
- Update webdriver.py. [urtow]

  Start_y - y-coordinate for start, not end


v0.10 (2014-09-24)
------------------
- Bump version. [Isaac Murchie]
- Removed complex_find, added get_settings, update_settings. [Jonah
  Stiennon]
- Added start_activity and tests. [Eric Millin]
- Make long_press works with 'duration' parameter. [ianxiaohanxu]

  Add a new parameter 'duration = None' to _get_opts
- Added 'keyevent' since it is needed for Selendroid. [Payman Delshad]
- Add set_text method for Android. [Isaac Murchie]
- Typo fix! [Cass]
- Update README.md. [Johan Lundstroem]

  Verison -> Version
- Revert "Fix for #23: Re-add 'keyevent' temporarily." [Payman Delshad]

  This reverts commit ccbcaf809704bf1ac752d1b4446d1175b7434c36.


v0.9 (2014-07-07)
-----------------
- Bump version. [Isaac Murchie]
- Add some more tests, fix others. [Isaac Murchie]
- Add ConnectionType enum. [Isaac Murchie]
- Add methods for Android ime access. [Isaac Murchie]
- Add network connection methods. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Change call to single-gesture tap. [Isaac Murchie]
- Add strategy to hide_keyboard. [Isaac Murchie]
- Add necessary ios attributes. [Brad Pitcher]
- Add pull_file method. [Isaac Murchie]
- Add support for open_notifications. [Isaac Murchie]
- Fix for #23: Re-add 'keyevent' temporarily. [Payman Delshad]
- Fix keycode command. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Add optional argument 'language' to app_strings. [Isaac Murchie]
- Renamed keyevent to press_keycode and added long_press_keycode.
  [Payman Delshad]
- Bump version. [Isaac Murchie]
- Fix for Python 3. [Isaac Murchie]
- Numerous fixes. [Alexander Bayandin]

  1. fix comparation with None
  2. remove unused imports
  3. fix imports order (according to pep8)
  4. style fixes (according to pep8)
  5. another minor fixes
- Fix typos with context. [Alexander Bayandin]
- Fix typo in README (resolve #12) [Alexander Bayandin]
- Add context method for simplicity. [Isaac Murchie]
- Fix timing. [Isaac Murchie]
- Update zoom/pinch signatures. [Isaac Murchie]
- Remove tag name, use class. [Isaac Murchie]
- Don't send multitouch for single finger tap. [Isaac Murchie]
- Add find methods to WebElement. [Isaac Murchie]
- Miscellaneous fixes. [Isaac Murchie]
- Add reset and hide_keyboard. [Isaac Murchie]
- Fix setup for egg distro, and add install instructions. [Isaac
  Murchie]
- Add PyPi packaging setup. [Isaac Murchie]
- Add miscellaneous methods. [Isaac Murchie]
- Add touch and multi touch. [Isaac Murchie]
- Update desired caps. [Isaac Murchie]
- Add accessibility id locator strategy. [Isaac Murchie]
- Add Android UIAutomator locator strategy. [Isaac Murchie]
- Add iOS UIAutomation locator strategy. [Isaac Murchie]
- Add context methods. [Isaac Murchie]
- Basic module structure. [Isaac Murchie]


