default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: init
init: # install dependencies, get latest models.yaml
	cp ../../models.yaml ./data
	npm install

.PHONY: lint
lint:  # lint the code
	npm run lint

.PHONY: lint-fix
lint-fix: # lint and fix the code
	npm run lint:fix

.PHONY: test # run tests and report coverage
test:
	cp ../../models.yaml ./data
	npm run test:cov

.PHONY: build # create a build ready for distribution
build:
	cp ../../models.yaml ./data
	npm install
	npm run build
