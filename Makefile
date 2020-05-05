.PHONY: Commands for developers

isort:
	python -m isort $(ARGS) -rc .

autopep8:
	python -m autopep8 $(ARGS) -a -r -i .

pylint:
	python -m pylint $(ARGS) --rcfile .pylintrc appium test

mypy:
	python -m mypy appium test

unittest:
	python -m pytest test/unit/