Appium Python Client Plan
=========================

This library will be a simple extension of the official Python bindings, through
subclassing, to add the new methods. I would like to maintain the same package
structure, so that switching to the Appium library would be a matter of changing
the import.

The official client allows for three ways to interact with the server: with the
`selenium` class, with the `webdriver.Remote` class, and with specific browser
classes, which subclass `webdriver.Remote` in `webdriver.*` classes. It seems
like we would not need to update the browser classes for our use case, and the
first is for RC, which we don't support. Thus we can subclass the official
`webdriver.Remote` classes and add the new methods. Otherwise we would need to
use composition, since we have to change the base class and subclasses.

Usage will remain as it currently is, using the first two methods from above,
other than importing from Appium:

```python
from appium import webdriver

desired_caps = {}
# ...

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

print driver.get_window_size()
elem = driver.find_element_by_name('Graphics')
elem.click()
driver.quit()
```

As Selenium catches up, the methods can be seemlessly removed from the Appium
client. Any methods outside of the spec can remain and be used without issue,
should the user choose.
