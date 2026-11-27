### Preview the documentation

From the repository root:

```bash
cd docs
bash generate.sh
python -m http.server 1234 --directory _build/html
```

Open http://localhost:1234 in a browser. The Quickstart, guides, API index and
WebDriver module pages are maintained here. Sphinx generates the options pages
in `generated/` from the API index.

### Publishing

[appium/python-client-sphinx](https://github.com/appium/python-client-sphinx)
builds these sources and publishes the HTML with GitHub Pages.
