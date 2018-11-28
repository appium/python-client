Changelog
=========


(unreleased)
------------
- Update the release section in README. [Kazuaki MATSUO]
- Tweak release.sh. [Kazuaki MATSUO]
- Introduce gitchangelog to generate changelog. [Kazuaki MATSUO]
- Update readme. [Kazuaki MATSUO]
- Extract version number. [Kazuaki MATSUO]
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


