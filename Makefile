.PHONY: Commands for developers

.PHONY: check-all
check-all: check unittest

.PHONY: check
check: check-lint check-format

.PHONY: check-lint
check-lint:
	uv run ruff check .
	uv run mypy appium

.PHONY: check-format
check-format:
	uv run ruff format --check .

.PHONY: fix
fix: fix-lint fix-format

.PHONY: fix-lint
fix-lint:
	uv run ruff check --fix .

.PHONY: fix-format
fix-format:
	uv run ruff format .

.PHONY: install-uv
install-uv:
	@command -v uv >/dev/null 2>&1 || { \
		echo "Installing uv"; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
		if [ -n "$$GITHUB_PATH" ]; then \
			echo "PATH=$$HOME/.local/bin:$$PATH" >> $$GITHUB_PATH; \
		else \
			echo "Please restart your shell or run 'exec $$SHELL'"; \
		fi; \
	}

.PHONY: sync-dev
sync-dev:
	uv sync

.PHONY: unittest
unittest: ## Run unittest
	uv run pytest $(ARGS) test/unit/

.PHONY: help
help: ## Display this help screen
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
