### How to generate doc

```bash
$cd python-client/docs
$pip install -r requirements.txt
$bash generate.sh
```

### How to check generated doc

```bash
$cd python-client/docs
$bash generate.sh
$cd python-client/docs/_build/html
$python -m http.server 1234
```

Access to http://localhost:1234 on web browser


### How to deploy generated doc
See https://github.com/ki4070ma/python-client-sphinx#how-to-deploy for now
