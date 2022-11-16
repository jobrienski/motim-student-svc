.PHONY: audit setup build unit lint fix test snyk start clean help
SHELL := /bin/bash
DIR := $(PWD)

export POSTGRES_DB = studentsdb

setup: clean
	@pipenv install --dev

help:   # prints all make targets
	@cat Makefile | grep '^[^ ]*:' | grep -v '.PHONY' | grep -v help | sed 's/:.*#/#/' | column -s "#" -t

start: clean # runs the API
	ENVIRONMENT=development pipenv run uvicorn app.main:app --port 8001 --reload

unit:
	@scripts/run-python-tester.sh

lint: clean # lints all files
	@scripts/run-standard-linter.sh
	@scripts/run-python-linter.sh

fix:
	@scripts/run-standard-formatter.sh
	@scripts/run-python-formatter.sh

test: build clean # lint audit    # runs all tests
	@make db
	@make unit

clean:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +
	@rm -rf build/
	@rm -rf dist/
	@rm -rf .eggs/
	@find . -name '.pytest_cache' -type d -exec rm -rf {} +

migrate:
	@pipenv run alembic upgrade head

db: # bring up db
	@scripts/setup-test-postgres.sh
	@make migrate

audit:
	@scripts/run-python-auditor.sh

snyk:
	@scripts/run-standard-auditor.sh
