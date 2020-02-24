### How to generate doc

```bash
$cd python-client
$sphinx-apidoc -F -o docs/ appium/webdriver
$cd docs
$make html
```

### How to check generated doc

```bash
$cd python-client/docs/_build/html
$python -m http.server 1234
```

Access to `http://localhost:1234` on web browser


### Deploy generated doc
To be updated