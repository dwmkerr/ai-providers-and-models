default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: test # run unit tests only
test:
	(cd node && make test)
	(cd python && make test)
	(cd validate-schema && make validate-schema)

.PHONY: integration-test # run integration tests (requires API keys)
integration-test:
	(cd integration-test && make test)

.PHONY: build # create a build ready for distribution
build:
	(cd node && make build)
	(cd python && make build)
