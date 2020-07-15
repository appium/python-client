Changelog
=========


v1.0.2 (2020-07-15)
-------------------
- Bump 1.0.2. [Kazuaki Matsuo]
- Chore: Add the workaround to avoid service freezes on Windows (#552)
  [Mykola Mokhnach]
- Chore: add checking package file count comparison in release script
  (#547) [Kazuaki Matsuo]

  * chore: Add file count in release script

  * use f string for Python 3 :P

  * handle exit in method
- Update changelog for 1.0.1. [Kazuaki Matsuo]


v1.0.1 (2020-05-18)
-------------------

Fix
~~~
- Broken package (#545) [Kazuaki Matsuo]

  * add appium/webdriver/py.typed in find_packages

  * fix

Other
~~~~~
- Bump 1.0.1. [Kazuaki Matsuo]
- Update changelog for 1.0.0. [Kazuaki Matsuo]


v1.0.0 (2020-05-16)
-------------------

New
~~~
- Feat: Added Makefile (#530) [Mori Atsushi]

  * Created setup.cfg

  * Updated lib ver for pre-commit

  * Fix ci.sh to set failure even when one command failed

  * Fix pylint error

  * Add help to Makefile

  * Update README

  * Add check-all command
- Feat: Merge python3 branch to master (#526) [Hannes Hauer, Hannes
  Hauer <hanneshauer@beeware.at>    * chore: Update readme and
  gitchangelog section role (#524) (#525)    * chore: tweak changelog
  filter    * address stoping Python 2 support    * 2 instead of 2.0...
  * tweak readme    * Revert some unexpected changes    * review
  comments    * Changed bound for TypeVar    * Fix crashing ci    *
  Remove beta    Co-authored-by: dependabot-preview[bot]
  <27856297+dependabot-preview[bot]@users.noreply.github.com>, Kazuaki
  Matsuo, Kazuaki Matsuo, Mori Atsushi, Mykola Mokhnach, Mykola
  Mokhnach, Nrupesh Patel, Nrupesh Patel, Venkatesh, Venkatesh]

  * Drop py2 support (#478)

  * Drop py2 support

  * Support 3.7+

  * Add explicit type declarations (#482)

  * Fixed mypy warning: touch_action.py

  * Fixed mypy warning: multi_action.py

  * Fixed mypy warning: extensions/android

  * Fixed mypy warning: extensions/search_context

  * Updated

  * Revert some changes to run unit test

  * Review comments

  * Updates

  * Updates

  * Add mypy check to ci.sh

  * Add mypy to Pipfile

  * Updates

  * Update README

  * Revert unexpected changes

  * Updates Dict

  * Revert unexpected changes

  * Updates

  * Review comments

  * Review comments

  * tweak

  * Restore and modify changes

  * Fix wrong return type

  * Add comments

  * Revert unexpected changes

  * Fix mypy error

  * updates

  * Add mypy to pre-commit (#485)

  * chore: Applied some py3 formats (#486)

  * Removed unused import

  * Removed unnecessary codes

  * Applied f'' format instead ''.format()

  * Fixes

  * tweak

  * chore: Fix mypy errors under test folder (#487)

  * Fix mypy errors under test folder

  * Add mypy check for test folder to pre-commit

  * Add mypy check to ci

  * chore: Remove unittest dependency (#488)

  * Removed unnecessary codes from calling super

  * Removed unittest dependency

  * Upgrade the dependencies to the latest

  * Removed unused args

  * Review comments

  * Update mock requirement from ~=3.0 to ~=4.0 (#502)

  Updates the requirements on [mock](https://github.com/testing-cabal/mock) to permit the latest version.
  - [Release notes](https://github.com/testing-cabal/mock/releases)
  - [Changelog](https://github.com/testing-cabal/mock/blob/master/CHANGELOG.rst)
  - [Commits](https://github.com/testing-cabal/mock/compare/3.0.0...4.0.0)

  Signed-off-by: dependabot-preview[bot] <support@dependabot.com>

  * Add 'from' to except (#503)

  * Update pre-commit requirement from ~=1.21 to ~=2.1 (#506)

  Updates the requirements on [pre-commit](https://github.com/pre-commit/pre-commit) to permit the latest version.
  - [Release notes](https://github.com/pre-commit/pre-commit/releases)
  - [Changelog](https://github.com/pre-commit/pre-commit/blob/master/CHANGELOG.md)
  - [Commits](https://github.com/pre-commit/pre-commit/compare/v1.21.0...v2.1.0)

  Signed-off-by: dependabot-preview[bot] <support@dependabot.com>

  * doc: Add script to generate sphinx doc  (#508)

  * Add quickstart template files

  * Update conf file

  * Update

  * Update settings

  * Change project name

  * Add script to generate docs

  * Changed header title

  * Add new line to usage section

  * Add py.typed file(PEP561)

  * Replace \n with new line

  * tweak

  * Use sphinx format for tables

  * Rebase python3 branch with master (#522)

  * Update pytest-cov requirement from ~=2.6 to ~=2.8 (#489)

  Updates the requirements on [pytest-cov](https://github.com/pytest-dev/pytest-cov) to permit the latest version.
  - [Release notes](https://github.com/pytest-dev/pytest-cov/releases)
  - [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
  - [Commits](https://github.com/pytest-dev/pytest-cov/compare/v2.6.0...v2.8.1)

  Signed-off-by: dependabot-preview[bot] <support@dependabot.com>

  * Update autopep8 requirement from ~=1.4 to ~=1.5 (#490)

  Updates the requirements on [autopep8](https://github.com/hhatto/autopep8) to permit the latest version.
  - [Release notes](https://github.com/hhatto/autopep8/releases)
  - [Commits](https://github.com/hhatto/autopep8/compare/v1.4...v1.5)

  Signed-off-by: dependabot-preview[bot] <support@dependabot.com>

  * Update tox-travis requirement from ~=0.11 to ~=0.12 (#491)

  Updates the requirements on [tox-travis](https://github.com/tox-dev/tox-travis) to permit the latest version.
  - [Release notes](https://github.com/tox-dev/tox-travis/releases)
  - [Changelog](https://github.com/tox-dev/tox-travis/blob/master/HISTORY.rst)
  - [Commits](https://github.com/tox-dev/tox-travis/compare/0.11...0.12)

  Signed-off-by: dependabot-preview[bot] <support@dependabot.com>

  * Update tox requirement from ~=3.6 to ~=3.14 (#494)

  Updates the requirements on [tox](https://github.com/tox-dev/tox) to permit the latest version.
  - [Release notes](https://github.com/tox-dev/tox/releases)
  - [Changelog](https://github.com/tox-dev/tox/blob/master/docs/changelog.rst)
  - [Commits](https://github.com/tox-dev/tox/compare/3.6.0...3.14.3)

  Signed-off-by: dependabot-preview[bot] <support@dependabot.com>

  * chore: Fix find_by_images_tests.py (#495)

  * chore: Fix find_by_images_tests.py

  * Add installation opencv4nodejs

  * Fix typo

  * Add taking screen record to find_by_image_test

  * Fix errors on the emulator

  * Remove unused imports

  * feat: Add viewmatcher (#480)

  * Add android view matcher as strategy locator

  * Add docstring

  * Add functional test

  * Remove find_elements_by_android_data_matcher

  * Fix docstring

  * tweak docstring

  * Bump 0.50

  * Update changelog for 0.50

  * Fix flaky functional tests (#473)

  * Run all tests

  * Fix apk file path

  * Skip find_element_by_image test cases

  * Skip context switching test

  * Skip multi tap test on CI

  * Change strategy for waiting element

  * Add functions for same steps

  * Restore unexpected changes

  * Fix touch_action_tests

  * Fix

  * Fix
  Fix test_driver_swipe

  * fix

  * Create _move_to_[target_view]

  * [test_driver_swipe] Add wait

  * feat: Add idempotency key header to create session requests (#514)

  * feat: Override send_keys without file upload function (#515)

  * add send_keys_direct

  * override send_keys

  * tune

  * add unittest instead of functional test

  * tweak syntax

  * Bump 0.51

  * Update changelog for 0.51

  * test: Fix test_clear flaky functional test (#519)

  * test: Add unit test for set_value (setImmediateValue) (#518)

  * chore: Fix int - str comparison error in ios desired capabilities (#517)

  if number >= PytestXdistWorker.COUNT:

Fix
~~~
- Tune mixin types, so linters could recognize them better (#536)
  [Mykola Mokhnach]

Test
~~~~
- Test: Add appium_service functional test (#531) [Mori Atsushi]

  * Add appium_service functional test

  * Fix expressions

Other
~~~~~
- Bump 1.0.0. [Kazuaki Matsuo]
- Chore: Updates docstring (#533) [Mori Atsushi]

  * Updates docstring

  * Add description to Returns field

  * Remove type from docstring

  Since type hint already added to args

  * Set default lang to en

  * Change usage style in docstring

  * Updates

  * Remove rtype

  unnecessary anymore since type hint works for auto completion

  * tweak

  * Update return type

  * Restore types for keyword args

  * Remove types from Return field

  Except for property and TypeVar
- Chore: Remove  saucetestcase from the client (#539) [Mykola Mokhnach]
- Chore: add py.typed in package, add maintainers (#538) [Kazuaki
  Matsuo]
- Docs: Update documentation (#527) [Kazuaki Matsuo]

  * Chore: correct license, update readme

  * cleanup

  * docs: update the url of documentation
- Chore: Update readme and gitchangelog section role (#524) [Kazuaki
  Matsuo]

  * chore: tweak changelog filter

  * address stoping Python 2 support

  * 2 instead of 2.0...

  * tweak readme
- Update changelog for 0.52. [Kazuaki Matsuo]


v0.52 (2020-04-23)
------------------

Fix
~~~
- Handling of dictionary-values in WebElement.get_attribute() (#521)
  [Hannes Hauer]

Test
~~~~
- Test: Add unit test for set_value (setImmediateValue) (#518) [Nrupesh
  Patel]
- Test: Fix test_clear flaky functional test (#519) [Nrupesh Patel]

Other
~~~~~
- Bump 0.52. [Kazuaki Matsuo]
- Chore: Fix int - str comparison error in ios desired capabilities
  (#517) [Venkatesh]

  if number >= PytestXdistWorker.COUNT:
- Update changelog for 0.51. [Kazuaki Matsuo]


v0.51 (2020-04-12)
------------------

New
~~~
- Feat: Override send_keys without file upload function (#515) [Kazuaki
  Matsuo]

  * add send_keys_direct

  * override send_keys

  * tune

  * add unittest instead of functional test

  * tweak syntax
- Feat: Add idempotency key header to create session requests (#514)
  [Mykola Mokhnach]

Fix
~~~
- Fix flaky functional tests (#473) [Mori Atsushi]

  * Run all tests

  * Fix apk file path

  * Skip find_element_by_image test cases

  * Skip context switching test

  * Skip multi tap test on CI

  * Change strategy for waiting element

  * Add functions for same steps

  * Restore unexpected changes

  * Fix touch_action_tests

  * Fix

  * Fix
  Fix test_driver_swipe

  * fix

  * Create _move_to_[target_view]

  * [test_driver_swipe] Add wait

Other
~~~~~
- Bump 0.51. [Kazuaki Matsuo]
- Update changelog for 0.50. [Kazuaki Matsuo]


v0.50 (2020-02-10)
------------------

New
~~~
- Feat: Add viewmatcher (#480) [Mori Atsushi]

  * Add android view matcher as strategy locator

  * Add docstring

  * Add functional test

  * Remove find_elements_by_android_data_matcher

  * Fix docstring

  * tweak docstring

Test
~~~~
- Ci: Take screen record as evidence (#481) [Mori Atsushi]

  * Take screen record for android

  * Take screen record for iOS

  * Save screen record for iOS

Other
~~~~~
- Bump 0.50. [Kazuaki Matsuo]
- Chore: Fix find_by_images_tests.py (#495) [Mori Atsushi]

  * chore: Fix find_by_images_tests.py

  * Add installation opencv4nodejs

  * Fix typo

  * Add taking screen record to find_by_image_test

  * Fix errors on the emulator

  * Remove unused imports
- Update tox requirement from ~=3.6 to ~=3.14 (#494) [dependabot-
  preview[bot]]

  Updates the requirements on [tox](https://github.com/tox-dev/tox) to permit the latest version.
  - [Release notes](https://github.com/tox-dev/tox/releases)
  - [Changelog](https://github.com/tox-dev/tox/blob/master/docs/changelog.rst)
  - [Commits](https://github.com/tox-dev/tox/compare/3.6.0...3.14.3)
- Update tox-travis requirement from ~=0.11 to ~=0.12 (#491)
  [dependabot-preview[bot]]

  Updates the requirements on [tox-travis](https://github.com/tox-dev/tox-travis) to permit the latest version.
  - [Release notes](https://github.com/tox-dev/tox-travis/releases)
  - [Changelog](https://github.com/tox-dev/tox-travis/blob/master/HISTORY.rst)
  - [Commits](https://github.com/tox-dev/tox-travis/compare/0.11...0.12)
- Update autopep8 requirement from ~=1.4 to ~=1.5 (#490) [dependabot-
  preview[bot]]

  Updates the requirements on [autopep8](https://github.com/hhatto/autopep8) to permit the latest version.
  - [Release notes](https://github.com/hhatto/autopep8/releases)
  - [Commits](https://github.com/hhatto/autopep8/compare/v1.4...v1.5)
- Update pytest-cov requirement from ~=2.6 to ~=2.8 (#489) [dependabot-
  preview[bot]]

  Updates the requirements on [pytest-cov](https://github.com/pytest-dev/pytest-cov) to permit the latest version.
  - [Release notes](https://github.com/pytest-dev/pytest-cov/releases)
  - [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst)
  - [Commits](https://github.com/pytest-dev/pytest-cov/compare/v2.6.0...v2.8.1)
- Chore: add try/catch in release script (#479) [Kazuaki Matsuo]

  * Add m and try/catch in pushing

  * fix error message

  * remove -m since it does not work for this usage
- [CI] Run with iOS 13.3 and Xcode 11.3 (#477) [Mori Atsushi]

  * [CI] Run with iOS 13.3 and Xcode 11.3

  * Skip the case which has problem on Xcode 11.3

  * Update FyndByIOClassChainTests along to iOS13

  * Update FyndByElementWebelementTests along to iOS13

  * Update KeyboardTests along to iOS13

  * Update webdriver_tests along to iOS13

  * Run test_find_element_by_isvisible with simpleIsVisibleCheck caps

  * Run test_hide_keyboard_no_key_name

  * Remove unused codes

  * [Readme] py.test -> pytest
- Update changelog for 0.49. [Kazuaki Matsuo]


v0.49 (2019-12-24)
------------------

New
~~~
- Add IME unittest (#475) [Mori Atsushi]
- Add new locator strategy find_elements_by_windows_uiautomation and
  test. [Manoj Kumar]
- Add new locator strategy find_element_by_windows_uiautomation. [Manoj
  Kumar]

Fix
~~~
- Fix functional test broken by previous commit. [Manoj Kumar]
- Fix CI (Failed iOS) (#460) [Mori Atsushi]

  * Fix CI (Failed iOS)

  * Fix variable name

Other
~~~~~
- Bump 0.49. [Kazuaki Matsuo]
- Move session/execute_mobile commands to mixin class (#471) [Mori
  Atsushi]

  * Fix get_all_sessions

  * Revert changes

  * Move execute_mobile_command codes to mixin class

  * Update docstring

  It's same to webdriver.py

  * Use /sessions as endpoint for all_sessions

  https://github.com/appium/appium-base-driver/blob/master/docs/mjsonwp/protocol-methods.md

  * Delete unnecessary codes
- Replace apk for functional test (#470) [Mori Atsushi]

  * Replace apk for functional test

  https://github.com/appium/android-apidemos/releases/tag/v3.1.0

  * Use sdkVer 27

  * Update app package name

  * Fix: can't find android device

  * review comments

  * tweak
- Support for log_event and get_events command (#469) [Mori Atsushi]

  * Use appium/events as endpoint to get events

  * Removed unnecessary codes

  * Update unittest along to changes

  * Update docstring

  * Created LogEvents class

  * Support log_event

  * Add unittest for log_event

  * Add functional test for log_event and get_event

  * review comments

  * Restore events API

  * Add type as arg to get_events

  * tweak

  * Removed type arg from get_events

  It isn't implemented yet for now

  * Add type arg to get_event

  The value isn't passed to the server for now.

  * Updated along to type
- Cleaned up test codes (#466) [Mori Atsushi]

  * Deleted unnecessary codes

  * Move functional tests to correct class

  * Move some tests

  * Created search_context/windows_test

  * [functional] Created search_context package

  * Remove class method decolator

  * Fix import error

  * Add BaseTestCase for ios functional testcases

  * Add test_helper for android functional test

  * Add __init__.py

  * Deleted unused imports
- Move search context methods from webdriver and webelement to
  search_context (#461) [Mori Atsushi]

  * Move ios search context methods to search_context file

  * Move android search text methods

  * Move windows search context

  * Move mobile search context

  * Divided search_context into each class

  * Move custom and image methods

  * Move contents in search_context.py to __init__.py

  * Add rtype to each docstring for auto completion in IDE

  * Add comments
- [CI] Run functional tests nightly (#463) [Mori Atsushi]

  * [CI] Run functional tests nightly

  * Extend timeout to wait for 2nd session created

  * Skip flaky test_all_sessions
- Revert some changes to fix broken codes (#462) [Mori Atsushi]

  * Revert some changes

  * Fix typo
- Move commands from webdriver as mixins class (#459) [Manoj Kumar]

  * move to mixins class

  * Create common class with its tests

  * incorporating PR comments
- Update changelog for 0.48. [Kazuaki Matsuo]
- Bump 0.48. [Kazuaki Matsuo]


v0.48 (2019-10-22)
------------------

New
~~~
- Add docs on start activity with args. [Manoj Kumar]
- Add unit tests Activate app. [Manoj Kumar]
- Add unit tests for keyboard API (#452) [Manoj Kumar]

  * Add Unit tests for Keyboard API

  * incorporating review comments

  * change per review comment
- Feat: Adding getAllSessions (#446) [Manoj Kumar]

  * Adding getAllSessions

  * adjust per lint

  * fix comments
- Add downloads badge (#441) [Mori Atsushi]

Fix
~~~
- Fix docstring, add getting available port number (#448) [Kazuaki
  Matsuo]

  * fix docstring, add getting available port number

  * add WebDriverWait

  * define custom wait

  * move get available port in another module

  * follow python wait condition name
- Fix CI fails (Updated iOS ver) (#440) [Mori Atsushi]

  * Updated iOS ver to fix CI fails

  * Update capability for safari test on ios

  * Fix travis CI fails
- Fix CI fails (#436) [Mori Atsushi]

  * Skip taking the screenshot not in CI

  * Skip py38 on travis
- Fix isort behavior for mock (#432) [Mori Atsushi]

  * Fix isort behavior for mock

  * Add guide to add 3rd party modules to isort conf

  * Add guide for docstrings

  * Delete unnecessary codes
- Fix android flaky tests (#413) [Mori Atsushi]

  * Fix android flaky tests

  * Use androidSdkVer 27 for emulator

  * Skip find_by_accessibility_id, find_by_uiautomator

  * Changed from https://github.com/ki4070ma/python-client/pull/5

  * Add save_appium_log.yml

  * Don't run flaky tests on CI

  * Rename class name

Test
~~~~
- Test: Add unit tests for application_tests (#454) [Manoj Kumar]

  * Add unit tests for application_tests

  * change body values to be empty
- Test: add Unit tests currentPackage (#453) [Manoj Kumar]
- Test: add unit test unlock (#450) [Manoj Kumar]
- Ci: try run all scripts and exit 1 when something fails (#431)
  [Kazuaki Matsuo]

  * try run all scripts and exit 1 when something fails

  * ignore link in Python 3.7 because of runtime error

Other
~~~~~
- Docs: Minor fix in README (#445) [Aliakbar]
- AndroidKey class for Key Codes added. (#443) [Aliakbar]

  * AndroidKey class for Key Codes added.

  AndroidKey enum from java client ported. Instead of using unreadable numbers in code we can use these constant in order to write more readable code.

  * Android native key test

  Test for native key module which contains key codes for android keys.

  * Fixed # sign in comment instead of *

  * Change returns

  Instead of `if` and two return statements.

  * Used AndroidKey.XXX instead of numbers in tests

  * Make fuctions similar to  is_gamepad_button

  Used a similar sentence format for similar functions as is_gamepad_button.

  * Make function names as is in java-client

  * Underscore in the beginning of constant removed
- Run unittest with python3.8 (#433) [Mori Atsushi]
- Bump 0.47. [Kazuaki Matsuo]
- Update changelog for 0.47. [Kazuaki Matsuo]


v0.47 (2019-08-22)
------------------

New
~~~
- Add events property (#429) [Dan Graham]

  * add GET_SESSION

  * add events property, this property will get the current information of the session and get the events timings

  * add method for getting session_capabilities

  * update docstring

  * apply isort
- Add screenrecord unittest (#426) [Mori Atsushi]

  * Fix wrong docstring

  * Add screen_record unittest

  * Rename class names

  * Move test files

  * Fix docstring
- Add videoFilters option documentation (#419) [Mykola Mokhnach]
- Add remote_fs unittest (#410) [Mori Atsushi]

  * Add test_push_file unittest

  * Add test_pull_file unittest

  * Add remote_fs error cases unittest

Fix
~~~
- CI doesn't fail even if autopep8 makes changes (#422) [Mori Atsushi]

  * Fix: CI doesn't fail even if autopep8 makes changes

  * Fix: CI failure

Other
~~~~~
- Change altitude optional as arg for set_location (#415) [Mori Atsushi]

  * Change altitude optional as arg for set_location

  * Add comments

  * review comments
- Update docstring (#407) [Mori Atsushi]

  * Remove import error on pycharm

  And update docstring

  * Update docstring

  * Update docstring

  * Fix import error

  * fix

  * fix import order

  * tweak
- Update changelog for 0.46. [Kazuaki Matsuo]


v0.46 (2019-06-27)
------------------
- Bump 0.46. [Kazuaki Matsuo]
- Bug fix joining path in _get_main_script (#408) [Nicholas Frederick]
- Update changelog for 0.45. [Kazuaki Matsuo]


v0.45 (2019-06-26)
------------------

New
~~~
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
- Add unit test for open_notifications (#398) [tabatask]

Other
~~~~~
- Bump 0.45. [Kazuaki Matsuo]
- Moving reset method from WebDriver to Applications (#399) [Mayura]
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
- Fix ios functional tests failed (#385) [Mori Atsushi]

  * Fix safari test(iOS)

  * Fix: find_by_ios_predicate

  * Delete find_by_uiautomation_tests

  since uiautomation is deprecated

  * Move non test files

  * Replace test app with the latest

  * Fix tests failed along to replaced test app

  * review comments

Other
~~~~~
- Bump 0.44. [Kazuaki Matsuo]
- Support get_display_density (#388) [Mori Atsushi]

  * Support get_display_density

  * Add get_display_density unittest

  * Add api doc

  * Add return description to api doc
- Support set_network_speed (#386) [Mori Atsushi]

  * Support set_nework_speed

  * Add set_network_speed unittest

  * Add api doc

  * revert unexpected change

  * revert change
- Update changelog for 0.43. [Kazuaki Matsuo]


v0.43 (2019-05-18)
------------------

New
~~~
- Add assertions for w3c (#384) [Kazuaki Matsuo]
- Add isort to pre-commit (#379) [Mori Atsushi]

  * Add isort to pre-commit

  * Add isort.conf

  * Applied isort for test/unit

  * Add current dir to isrot arg

  * Add check to ci.sh

  * Use exit code for condition check in ci.sh

Fix
~~~
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

Other
~~~~~
- Bump 0.43. [Kazuaki Matsuo]
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
- Move android commands to android package (#371) [Mori Atsushi]

  * Reorder mobilecommands

  * Move android commands to android package

  * Update setup.py to include added packages

  * Changed find_packages to whitelist style
- Update changelog for 0.42. [Kazuaki Matsuo]


v0.42 (2019-05-10)
------------------

New
~~~
- Add return value. [Atsushi Mori]
- Add set_power_ac unittest. [Atsushi Mori]
- Added set_power_capacity unittest. [Atsushi Mori]

Fix
~~~
- Fix functional tests failed (android, appium_tests) (#366) [Mori
  Atsushi]

  * Fix test failed: test_send_keys, test_screen_record

  * Fix test failed: test_update_settings

  * Fix test failed: test_start_activity_other_app

  * Move and rename helper package

  * Update along to review comments

  * Add return value to wait_for_element
- Fix poll_url in Python 3 (#370) [Kazuaki Matsuo]
- Fix functional tests failed (#364) [Mori Atsushi]

  * Fix test failed: element_location_in_view, set_text

  * Fix test failed: test_push_file

  * Merge test_pull_test into test_push_test

  * Fix test failed: test_pull_folder

  * Enable running by both py2 and py3

  * Removed unnecessary codes

  * Remove magic number

Other
~~~~~
- Bump 0.42. [Kazuaki Matsuo]
- Support get_performance_data, get_performance_data_types (#368) [Mori
  Atsushi]

  * Support get_performance_data, get_performance_data_types

  * Add api doc

  * Add performance unittest

  * Tweak

  * Update api doc
- Support set_gsm_voice (#367) [Mori Atsushi]

  * Support set_gsm_voice

  * Add set_gsm_voice unittest

  * Fix typo
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
- Update api doc. [Atsushi Mori]
- Support set_power_ac. [Atsushi Mori]
- Support set_power_capacity. [Atsushi Mori]
- Update changelog for 0.41. [Kazuaki Matsuo]
- Bump 0.41. [Kazuaki Matsuo]


v0.41 (2019-04-23)
------------------

New
~~~
- Add send sms support (#351) [Mori Atsushi]

  * Support sendSms function

  * Added api doc

  * Add sms unittest

  * Revert unexpected changes

  * Update api doc
- Add pixelFormat in docstring (#346) [Kazuaki Matsuo]
- Add fingerprint unittest (#345) [Mori Atsushi]
- Add shake unittest (#344) [Mori Atsushi]

Fix
~~~
- Fix True/False in image settings, add boolean value in settings test
  (#352) [Kazuaki Matsuo]

  * Fix True/False in image settings, add boolean value in settings test

  * use is for boolean

Other
~~~~~
- Make keep alive True by default (#348) [Kazuaki Matsuo]
- Move settings to mixin classes (#347) [Mori Atsushi]
- Update changelog for 0.40. [Kazuaki Matsuo]


v0.40 (2019-03-14)
------------------

Fix
~~~
- Fix RuntimeError: maximum recursion depth exceeded in cmp happened
  (#343) [Kazuaki Matsuo]

  * fix maximum recursion depth exceeded in sub classes

  * add docstring

  * add comparison of a number of commands

  * use issubclass to ensure the class is sub

Other
~~~~~
- Bump 0.40. [Kazuaki Matsuo]
- Update missing changelog in 0.39. [Kazuaki Matsuo]


v0.39 (2019-02-27)
------------------

New
~~~
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

Other
~~~~~
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

New
~~~
- Add AppiumConnection to customise user agent (#327) [Kazuaki Matsuo]
- Add a test for reset (#326) [Kazuaki Matsuo]
- Add a simple class to control Appium execution from the client code
  (#324) [Mykola Mokhnach]
- Add pressure option (#322) [Kazuaki Matsuo]

  * add pressure option

  * add a test, tweak comment and the method

  * fix typo
- Add a test case using another session id (#320) [Kazuaki Matsuo]

Fix
~~~
- Fix passing options to screen record commands (#330) [Mykola Mokhnach]

Other
~~~~~
- Cast set_location arguments to float (#332) [Mykola Mokhnach]
- Update changelog for 0.36. [Kazuaki MATSUO]
- Bump 0.36. [Kazuaki MATSUO]


v0.36 (2019-01-18)
------------------
- Bump 0.36. [Kazuaki MATSUO]
- Import keyboard, add tests (#319) [Kazuaki Matsuo]
- Update changelog for 0.35. [Kazuaki MATSUO]


v0.35 (2019-01-17)
------------------

New
~~~
- Add location unittest (#317) [Mori Atsushi]

  * Add test_location

  * Add test_set_location

  * Add test_toggle_location_services
- Add settings unittest (#315) [Mori Atsushi]

  * Add settings unittest

  * Remove unused import
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
- Add precommit (#304) [Kazuaki Matsuo]

  * add pre-commit hook

Fix
~~~
- Fixing broken pypi long description rendering (#303) [Prabhash]

  reference: https://packaging.python.org/guides/making-a-pypi-friendly-readme

  Tested at https://pypi.org/project/delayed-assert
- Fix overridden mixin method call (#297) [Mykola Mokhnach]

Other
~~~~~
- Bump 0.35. [Kazuaki MATSUO]
- Move device_time to a mixin class (#314) [Mori Atsushi]
- Define getting httpretty request body decoded by utf-8 (#313) [Kazuaki
  Matsuo]

  * define httpretty_last_request_body

  * replace the order

  * update

  * rename
- Move action and keyboard helpers to mixin classes (#307) [Mykola
  Mokhnach]
- Extract more webdriver methods into specialized mixin classes (#302)
  [Mykola Mokhnach]
- Move specialized method groups to mixin classes (#301) [Mykola
  Mokhnach]
- Update changelog for 0.34. [Kazuaki MATSUO]


v0.34 (2018-12-18)
------------------

Fix
~~~
- Fix missing package, missing commands and a test (#296) [Kazuaki
  Matsuo]

  * add extensions into package

  * add tests for context to make sure it loads

  * move command definition from extensions to root

Other
~~~~~
- Bump 0.34. [Kazuaki MATSUO]
- Update changelog for 0.33. [Kazuaki MATSUO]


v0.33 (2018-12-18)
------------------

New
~~~
- Add newline in release script because of autopep8 (#292) [Kazuaki
  Matsuo]

Other
~~~~~
- Bump 0.33. [Kazuaki MATSUO]
- Move read version (#294) [Kazuaki Matsuo]
- Update changelog for 0.32. [Kazuaki MATSUO]


v0.32 (2018-12-18)
------------------

New
~~~
- Add unit tests for isLocked Library (#288) [Venkatesh Singh]

  * Add unit tests for isLocked Lib

  * moved isLocked library tests in lock.py
- Add unit test for lock lib (#287) [Venkatesh Singh]

  * Add unit test for lock lib

Fix
~~~
- Fixed few failing tests in appium_tests.py (#278)
  [RajeshkumarAyyadurai]

  * fixed few failing tests in appium_tests.py

  * updated few tests in appium_tests.py by removing uiautomator strategy
- Fixed failing tests in find_by_accessibility_id_tests.py.
  [RajeshkumarAyyadurai]

Other
~~~~~
- Bump 0.32. [Kazuaki MATSUO]
- Split driver methods into mixin classes (#291) [Mykola Mokhnach]
- Run with tox on travis (#290) [Kazuaki Matsuo]

  * run with tox on travis

  * update readme
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

New
~~~
- Add release section in readme. [Kazuaki MATSUO]

Fix
~~~
- Fix python3 set_clipboard error (#267) [Kazuaki Matsuo]

  * fix python3 set_clipboard error

  * apply formatter

Other
~~~~~
- V0.30. [Kazuaki MATSUO]


v0.29 (2018-10-30)
------------------

New
~~~
- Add an endpoint for pressing buttons (#262) [Alex]
- Add custom locator strategy (#260) [Jonathan Lipps]
- Add a duration for scroll for ios (#256) [Kazuaki Matsuo]

  * add a duration for scroll for ios

  * tweak default duration

  * apply autoformat

  * set 600 duration by default if it's w3c spec

  * skip wait if duration is none

  * add comment
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

Other
~~~~~
- V0.29. [Kazuaki MATSUO]
- Bump selenium 3.14.1, call RemoteCommand without workaround (#259)
  [Kazuaki Matsuo]

  * bump selenium 3.14.1, call RemoteCommand without workaround

  * make attributeValue check safe

  * define str = basestring for Python 2

  * apply formatter

  * add missing value check
- Update obsolete link for mobile json wire protocol spec. (#257)
  [Andrei Petre]
- Remove always_match and use first_match instead (#246) [Kazuaki
  Matsuo]

  remove always_match and use first_match instead
- Use normal element for find image by (#236) [Kazuaki Matsuo]

  * use normal element

  * get rid of png

  * get rid of imagelement.py

  * apply formatter
- Typo fix: finiding -> finding (#245) [Andrew Fuller]
- Tweak PyPi URLs and add a badge (#232) [Kazuaki Matsuo]


v0.28 (2018-07-13)
------------------

Fix
~~~
- Fix base64 encoded string (#231) [Kazuaki Matsuo]

Other
~~~~~
- V0.28. [Isaac Murchie]


v0.27 (2018-07-10)
------------------

New
~~~
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
- Add clipboard handlers (#209) [Mykola Mokhnach]

  * Add clipboard handlers

  * Fix documentation

  * fix options notation
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

Other
~~~~~
- V0.27. [Isaac Murchie]
- Set None as default value to lock device (#227) [Miguel Hernández]

  * Set 0 as default value to lock device

  * Set None as default value instead of 0
- Avoid setting coordinates to null for touch actions (#214) [Mykola
  Mokhnach]
- Change QUERY_APP_STATE request type to POST (#205) [Mykola Mokhnach]


v0.26 (2018-01-09)
------------------
- V0.26. [Isaac Murchie]


v0.25 (2018-01-09)
------------------

New
~~~
- Add method for getting current package. [Isaac Murchie]
- Add tests for ios class chain and rename methods a bit. [Kazuaki
  MATSUO]
- Add class chain. [Kazuaki MATSUO]
- Add toggleTouchIdEnrollment. [Dan Graham]

Fix
~~~
- Fix typos in the README. [Mel Shafer]

Other
~~~~~
- V0.25. [Isaac Murchie]
- Only if key_name, key, and strategy are None do we need to set the
  strategy to 'tapOutside'. This change allows setting just the strategy
  to some other value, like 'swipeDown'. (#181) [Daniel Freer]
- Correct a wording. [Kazuaki MATSUO]
- Create README.md. [Kazuaki Matsuo]
- Append class chain related descriptions. [Kazuaki MATSUO]
- Update README to include instructions for using iOS predicates. [Emil
  Petersen]
- Update docs for UIAutomation selector to include version requirement.
  [Emil Petersen]


v0.24 (2016-12-20)
------------------

New
~~~
- Added test cases for clear and find elements by ios predicate string.
  [ben.zhou]
- Added clear to driver. Added find elements by ios predicate string.
  [ben.zhou]

Other
~~~~~
- V0.24. [Isaac Murchie]
- DontStopAppOnReset instead of stopAppOnReset. [s.zubov]


v0.23 (2016-11-10)
------------------

New
~~~
- Added touchId to driver (#143) [Dan Graham]

  * Added touchId to driver

  Wrote a test for it (still need help running Python tests though). Updated capabilities to use iOS 10.1

Other
~~~~~
- V0.23. [Isaac Murchie]


v0.22 (2016-03-16)
------------------
- V0.22. [Isaac Murchie]
- Use id instead of elementId. [Isaac Murchie]


v0.21 (2016-01-20)
------------------

New
~~~
- Add device_time property. [Isaac Murchie]

Fix
~~~
- Fix saucetestcase to run under Python3. [Ling Lin]

  The module 'new' was removed. Instead of new.newclass, use type().

Other
~~~~~
- V0.21. [Isaac Murchie]
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

New
~~~
- Add string file argument to driver.app_strings. [Isaac Murchie]
- Add wait_activity method for webdriver. [zhaoqifa]
- Add el.location_in_view method. [Isaac Murchie]

Fix
~~~
- Fixed typographical error, changed accomodate to accommodate in
  README. [orthographic-pedant]
- Fix bug with monkeypatching. [Isaac Murchie]
- Fix to issue #71. [James Salt]
- Fix start_activity for Python 3.x. [Artur Tanistra]
- Fix start_activity for Python3. [Isaac Murchie]

Other
~~~~~
- V0.18. [Isaac Murchie]
- Remove dependency on enum. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Use WebDriverWait to implement wait_activity. [zhaoqifa]
- Make tap duration be handled as ms, not s. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Move monkeypatched set_value into WebElement. [Isaac Murchie]


v0.14 (2015-03-06)
------------------

Fix
~~~
- Fix issue with single tap. [Isaac Murchie]
- Fix handling of sauce test case so ImportError is suppressed. [Isaac
  Murchie]

Other
~~~~~
- Bump version. [Isaac Murchie]
- Bump version. [Isaac Murchie]


v0.12 (2015-01-13)
------------------

New
~~~
- Add base class for Sauce tests. [Isaac Murchie]
- Add remaining optional arguments to start_activity method. [Isaac
  Murchie]

Fix
~~~
- Fix package names for starting activity. [Isaac Murchie]

Other
~~~~~
- Bump version. [Isaac Murchie]
- Update README.md. [Mikhail Martin]

  Missing dot causes errors.
- Update webdriver.py. [urtow]


v0.11 (2014-11-14)
------------------

New
~~~
- Add toggle_location_services. [Isaac Murchie]

Other
~~~~~
- Bump version. [Isaac Murchie]
- Update webdriver.py. [urtow]

  Start_y - y-coordinate for start, not end


v0.10 (2014-09-24)
------------------

New
~~~
- Added start_activity and tests. [Eric Millin]
- Added 'keyevent' since it is needed for Selendroid. [Payman Delshad]
- Add set_text method for Android. [Isaac Murchie]

Other
~~~~~
- Bump version. [Isaac Murchie]
- Removed complex_find, added get_settings, update_settings. [Jonah
  Stiennon]
- Make long_press works with 'duration' parameter. [ianxiaohanxu]

  Add a new parameter 'duration = None' to _get_opts
- Typo fix! [Cass]
- Update README.md. [Johan Lundstroem]

  Verison -> Version
- Revert "Fix for #23: Re-add 'keyevent' temporarily." [Payman Delshad]

  This reverts commit ccbcaf809704bf1ac752d1b4446d1175b7434c36.


v0.9 (2014-07-07)
-----------------

New
~~~
- Add some more tests, fix others. [Isaac Murchie]
- Add ConnectionType enum. [Isaac Murchie]
- Add methods for Android ime access. [Isaac Murchie]
- Add network connection methods. [Isaac Murchie]
- Add strategy to hide_keyboard. [Isaac Murchie]
- Add necessary ios attributes. [Brad Pitcher]
- Add pull_file method. [Isaac Murchie]
- Add support for open_notifications. [Isaac Murchie]
- Add optional argument 'language' to app_strings. [Isaac Murchie]
- Add context method for simplicity. [Isaac Murchie]
- Add find methods to WebElement. [Isaac Murchie]
- Add reset and hide_keyboard. [Isaac Murchie]
- Add PyPi packaging setup. [Isaac Murchie]
- Add miscellaneous methods. [Isaac Murchie]
- Add touch and multi touch. [Isaac Murchie]
- Add accessibility id locator strategy. [Isaac Murchie]
- Add Android UIAutomator locator strategy. [Isaac Murchie]
- Add iOS UIAutomation locator strategy. [Isaac Murchie]
- Add context methods. [Isaac Murchie]

Fix
~~~
- Fix for #23: Re-add 'keyevent' temporarily. [Payman Delshad]
- Fix keycode command. [Isaac Murchie]
- Fix for Python 3. [Isaac Murchie]
- Fix typos with context. [Alexander Bayandin]
- Fix typo in README (resolve #12) [Alexander Bayandin]
- Fix timing. [Isaac Murchie]
- Fix setup for egg distro, and add install instructions. [Isaac
  Murchie]

Other
~~~~~
- Bump version. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Change call to single-gesture tap. [Isaac Murchie]
- Bump version. [Isaac Murchie]
- Renamed keyevent to press_keycode and added long_press_keycode.
  [Payman Delshad]
- Bump version. [Isaac Murchie]
- Numerous fixes. [Alexander Bayandin]

  1. fix comparation with None
  2. remove unused imports
  3. fix imports order (according to pep8)
  4. style fixes (according to pep8)
  5. another minor fixes
- Update zoom/pinch signatures. [Isaac Murchie]
- Remove tag name, use class. [Isaac Murchie]
- Don't send multitouch for single finger tap. [Isaac Murchie]
- Miscellaneous fixes. [Isaac Murchie]
- Update desired caps. [Isaac Murchie]
- Basic module structure. [Isaac Murchie]


