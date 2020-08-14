.PHONY: Commands for developers

.PHONY: check-all
check-all: ## Run all lint checks and unittest
	@echo "[Notice] If you'd like to run commands with same env to CI, please run \`tox\`."
	@bash ci.sh

.PHONY: isort
isort: ## Run isort
	python -m isort $(ARGS) -rc .

.PHONY: autopep8
autopep8: ## Run autopep8
	python -m autopep8 $(ARGS) -a -r -i .

.PHONY: pylint
pylint: ## Run pylint
    # TODO Remove --disable=E1136 when no errors in py39
	python -m pylint $(ARGS) --rcfile .pylintrc appium test --disable=E1136

.PHONY: mypy
mypy:  ## Run mypy
	python -m mypy appium test

.PHONY: unittest
unittest: ## Run unittest
	python -m pytest test/unit/

.PHONY: help
help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
