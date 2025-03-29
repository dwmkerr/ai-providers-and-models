default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: init
init: # install dependencies, get latest models.yaml
	cp ../../models.yaml ./src/ai_providers_and_models/data
	python -m pip install --upgrade pip
	pip install -r requirements-dev.txt
	pip install -e .

.PHONY: lint
lint:  # lint the code
	flake8 src/ tests/ examples/

.PHONY: lint-fix
lint-fix: # lint and fix the code
	black .

.PHONY: test # run tests and report coverage
test:
	coverage run -m pytest
	coverage xml -o artifacts/coverage/coverage.xml
	coverage report -m

.PHONY: build # create a build ready for distribution
build:
	rm -rf ./dist
	python -m build
