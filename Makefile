.PHONY: Commands for developers

.PHONY: isort
isort: ## Run isort
	python -m isort $(ARGS) -rc .

.PHONY: autopep8
autopep8: ## Run autopep8
	python -m autopep8 $(ARGS) -a -r -i .

.PHONY: pylint
pylint: ## Run pylint
	python -m pylint $(ARGS) --rcfile .pylintrc appium test

.PHONY: mypy
mypy:  ## Run mypy
	python -m mypy appium test

.PHONY: unittest
unittest: ## Run unittest
	python -m pytest test/unit/

.PHONY: help
help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
