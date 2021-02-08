.PHONY: Commands for developers

.PHONY: check-all
check-all: ## Run all lint checks and unittest
	@echo "[Notice] If you'd like to run commands with same env to CI, please run \`tox\`."
	@bash ci.sh

.PHONY: isort
isort: ## Run isort
	python -m isort $(ARGS) .

.PHONY: black
black: ## Run black
	python -m black $(ARGS) . -l 120 -S

.PHONY: pylint
pylint: ## Run pylint
    # TODO Remove --disable=E1136 when no errors in py39
	python -m pylint $(ARGS) --rcfile .pylintrc appium test --disable=E1136

.PHONY: mypy
mypy:  ## Run mypy
	python -m mypy appium test/functional

.PHONY: unittest
unittest: ## Run unittest
	python -m pytest ${ARGS} test/unit/

.PHONY: help
help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
