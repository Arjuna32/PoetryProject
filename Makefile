.SILENT:
# assumes that \program files\git\usr\bin is on path AND sh.exe in same folder is remove/renamed

#SHELL := pwsh
#.SHELLFLAGS := -Command

.PHONY: commands
commands:
	echo Default makefile commands
	cat Makefile | grep -i ".title=" | tail -n +2 | sed -e "s/.title=/ -\> /g" -e "s/^/\t/"

.PHONY: test
test.title=run pytest
test:
	poetry run pytest -v


.PHONY: lint
lint.title=run pylint on src folder
lint:
	echo Running pylint
	poetry run pylint ./bigcli

.PHONY: coverage
coverage.title=run coverage
coverage:
	poetry run coverage run --source=bigcli -m pytest && poetry run coverage report -m


.PHONY: all
all.title=run test lint coverage
all: test lint coverage
	@echo.
