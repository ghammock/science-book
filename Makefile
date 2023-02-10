# SciGuy Makefile
#
# Requires:
#   GNU Make >= 4.2
#   Python >= 3.8
#
# Examples:
#   # To show usage:
#   $ make
#
#   # To build the development environment:
#   $ make dev-install
#

IMG	= sciguy
SHELL := /bin/bash

RED = "\\e[31m"
GREEN = "\\e[32m"
RESET = "\\e[0m"

HAS_POETRY := $(shell command -v poetry &> /dev/null && echo 1 || echo 0)
HAS_MARKDOWNLINT := $(shell command -v markdownlint &> /dev/null && echo 1 || echo 0)

.PHONY: build
build:  ## Builds the project into a distribution
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Building the distributables...$(RESET)"
	@poetry build \
	  && echo -e "\n\t$(GREEN)Distribution files are in the dist/ directory$(RESET)" \
	  || echo -e "\n\t$(RED)An error occurred while building.  Check the output above for information$(RESET)"
else
	@echo -e "$(RED)You must install Poetry for this project$(RESET)"
endif

.PHONY: clean
clean:  ## Removes any cache, generated, and build directories
	@echo -e "$(RED)Removing cache, generated, and build directories...$(RESET)"
	@rm -rf .eggs/
	@rm -rf .mypy_cache/
	@rm -rf .pytest_cache/
	@rm -rf build/
	@rm -rf dist/
	@rm -rf docs/build/
	@rm -rf *.egg-info/
	@rm -rf tests/coverage/
	@rm -f .coverage*
	@find . -name "junit.*.xml" -delete
	@find . -name "coverage.xml" -delete
	@find . -type d -name "__pycache__" -not -regex "\./\.?venv/.*" -prune -exec rm -rf "{}" \;
	@find . -type d -name "node_modules" -not -regex "\./\.?venv/.*" -prune -exec rm -rf "{}" \;
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(RED)Removing virtual environment(s)...$(RESET)"
	@poetry env remove --all
endif
	@echo -e "$(GREEN)make clean succeeded$(RESET)"

.PHONY: coverage
coverage:  ## Runs unit tests with code coverage
ifeq ($(HAS_POETRY), 1)
	@poetry run pytest \
	    --junitxml junit.coverage.xml \
	    --cov=sciguy \
	    --cov-branch \
	    --cov-report=html:tests/coverage/html \
    	--cov-report=xml:tests/coverage/coverage.xml \
	    tests/
endif

.PHONY: dev-install
dev-install: export POETRY_VIRTUALENVS_IN_PROJECT=1
dev-install:  ## Uses Poetry to install all development packages
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Performing development installation...$(RESET)"
	@poetry install
else
	@echo -e "$(RED)You must install Poetry for this project$(RESET)"
endif

.PHONY: docs
docs: DOCS_BUILD_DIR = "./docs/build"
docs: DOCS_SOURCE_DIR = "./docs/src"
docs:  ## Builds the Sphinx documentation
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Building documentation...$(RESET)"
	@poetry run sphinx-build -b html -d $(DOCS_BUILD_DIR)/doctrees $(DOCS_SOURCE_DIR) $(DOCS_BUILD_DIR) \
	  && rm -f debug.log errors.log info.log warn.log
endif

.PHONY: docs-pdf
docs-pdf: DOCS_SOURCE_DIR = "./docs/src"
docs-pdf:  ## Builds the Sphinx documentation as a PDF
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Building documentation...$(RESET)"
	@poetry run sphinx-build -b latex $(DOCS_SOURCE_DIR) docs/latex \
	   && $(MAKE) -C docs/latex \
	   && mv docs/latex/*.pdf docs/ \
	   && rm -rf docs/latex \
	   && (echo -e "$(GREEN)PDF documents build successfully$(RESET)"; rm -rf debug.log errors.log info.log warn.log) \
	   || echo -e "$(RED)Error building PDF documents$(RESET)"
endif

.PHONY: format
format:  ## Uses black and isort to format Python files
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Formatting files...$(RESET)"
	@poetry run isort .
	@poetry run black .
else
	@echo -e "$(RED)You must install Poetry for this project$(RESET)"
endif

.PHONY: format-check
format-check:  ## Checks formatting (but does not modify files)
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Formatting check...$(RESET)"
	@poetry run black --check --diff .
else
	@echo -e "$(RED)You must install Poetry for this project$(RESET)"
endif

.PHONY: import-check
import-check:  ## Checks import order (but does not modify files)
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Import order check...$(RESET)"
	@poetry run isort --check --diff .
else
	@echo -e "$(RED)You must install Poetry for this project$(RESET)"
endif

.PHONY: lint
lint:  ## Performs style checking (linting)
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Linting Python Files...$(RESET)"
	@poetry run flake8 . || (echo -e "\n\t$(RED)Errors were detected in Python file linting$(RESET)"; false)
	@echo -e "\n$(GREEN)Linting YAML Files...$(RESET)"
	@poetry run yamllint . || (echo -e "\n\t$(RED)Errors were detected in YAML file linting$(RESET)"; false)
	@echo -e "\n"
else
	@echo -e "$(RED)You must install Poetry for this project$(RESET)"
endif

ifeq ($(HAS_MARKDOWNLINT), 1)
	@echo -e "$(GREEN)Linting Markdown Files...$(RESET)"
	@markdownlint --ignore "docs/pull_request_template.md" . \
	  || (echo -e "\n\t$(RED)Errors were detected in Markdown file linting$(RESET)"; false)
endif

.PHONY: publish
publish: export PYPIRC_PATH=${PYPIRC_PATH:~/.pypirc}
publish: build  ## Publishes the build artifacts to the artifactory
	@echo -e "$(GREEN)Checking artifacts for validity...$(RESET)"
	@python -m twine check dist/*
	@echo -e "$(GREEN)Uploading artifacts...$(RESET)"
	@python -m twine upload -r rseg-datascience --config-file $(PYPIRC_PATH) dist/* \
	  && echo -e "$(GREEN)Artifacts published successfully!$(RESET)" \
	  || (echo -e "$(RED)Artifact publishing failed!$(RESET)"; false)

.PHONY: sast-scan
sast-scan:  ## Run Static Application Security Testing (SAST) scans on the source code
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Performing SAST Scan...$(RESET)"
	@poetry run bandit --recursive --skip B101 src/sciguy/ \
	  && echo -e "$(GREEN)No security concerns detected.$(RESET)" \
	  || (echo -e "$(RED)Scans detected potential vulnerabilities.$(RESET)"; false)
else
	@echo -e "$(RED)You must install Poetry for this project$(RESET)"
endif

.PHONY: test
test:  ## Runs unit tests on the code
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Running unit tests...$(RESET)"
	@poetry run python -m pytest --junitxml junit.pytest.xml
else
	@echo -e "$(RED)You must install Poetry for this project$(RESET)"
endif

.PHONY: type-check
type-check:  ## Perform static type analysis on the source code
ifeq ($(HAS_POETRY), 1)
	@echo -e "$(GREEN)Type-checking the source code...$(RESET)"
	@poetry run mypy
else
	@echo -e "$(RED)You must install Poetry for this project$(RESET)"
endif

.PHONY: help
help:  ## Displays this help information
	@grep -E '^[a-zA-Z_-]+:(.*?## .*)?$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.DEFAULT_GOAL := help
