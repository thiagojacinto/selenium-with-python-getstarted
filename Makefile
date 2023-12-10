
# shell colors
COLOUR_GREEN=\033[0;32m
COLOUR_RED=\033[0;31m
COLOUR_BLUE=\033[0;34m
COLOUR_END=\033[0m

se-docker-up: #starts the docker containers set by containers/compose.yaml file:
	@echo "$(COLOUR_GREEN)UP Docker containers set by compose file ...$(COLOUR_END)"
	docker compose -f containers/compose.yaml up -d

se-docker-down: #terminates the docker containers set by containers/compose.yaml file:
	@echo "$(COLOUR_RED)DOWN Docker containers set by compose file ...$(COLOUR_END)"
	docker compose -f containers/compose.yaml down

se-docker-run-tests: #Running tests for Firefox, Chrome and Edge browsers from docker containers
	@echo "$(COLOUR_BLUE)Running tests for Firefox, Chrome and Edge browsers from docker containers ...$(COLOUR_END)"
	docker compose -f containers/compose.yaml exec python sh -c "SELENIUM_HOST=chrome pytest -vx --use-browser remote & SELENIUM_HOST=firefox pytest -vx --use-browser remote & SELENIUM_HOST=edge pytest -vx --use-browser remote"

se-docker-run-tests-firefox: #Running tests for Firefox browser from docker containers
	@echo "$(COLOUR_BLUE)Running tests for Firefox browser from docker containers ...$(COLOUR_END)"
	docker compose -f containers/compose.yaml exec python sh -c "SELENIUM_HOST=firefox pytest -vx --use-browser remote"

se-docker-run-tests-chrome: #Running tests for Chrome browser from docker containers
	@echo "$(COLOUR_BLUE)Running tests for Chrome browser from docker containers ...$(COLOUR_END)"
	docker compose -f containers/compose.yaml exec python sh -c "SELENIUM_HOST=chrome pytest -vx --use-browser remote "

se-docker-run-tests-edge: #Running tests for Edge browser from docker containers
	@echo "$(COLOUR_BLUE)Running tests for Edge browser from docker containers ...$(COLOUR_END)"
	docker compose -f containers/compose.yaml exec python sh -c "SELENIUM_HOST=edge pytest -vx --use-browser remote"


#: #########################################
#: ############ Help - Makefile ############
#: #########################################

help: # list all Makefile commands
	@echo "$(COLOUR_BLUE)These are all the avalaible commands ...$(COLOUR_END)"
	@echo ""
	@grep ': #' Makefile