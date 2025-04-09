default: help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: init
init: # install dependencies
	python -m pip install --upgrade pip
	pip install -r requirements.txt

.PHONY: validate-schema # valiate the models yaml against the schema
validate-schema:
	./validate.py ../../models.yaml ../models-schema.yaml
