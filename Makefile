.PHONY: Commands for developers

.PHONY: check-all
check-all: ## Run all lint checks and unittest
	@echo "[Notice] If you'd like to run commands with same env to CI, please run \`tox\`."
	@bash ci.sh

.PHONY: check
check: lint format

.PHONY: lint
lint:
	python -m ruff check .

.PHONY: format
format:
	python -m ruff format --check .

.PHONY: fix
fix: fix-lint fix-format

.PHONY: fix-lint
fix-lint:
	python -m ruff check --fix .

.PHONY: fix-format
fix-format:
	python -m ruff format .


.PHONY: unittest
unittest: ## Run unittest
	python -m pytest $(ARGS) test/unit/

.PHONY: help
help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
