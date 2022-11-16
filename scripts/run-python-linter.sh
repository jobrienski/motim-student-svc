#!/usr/bin/env bash
set -euo pipefail

echo "Running 'python linter'"

pipenv run flake8 --max-line-length=140
pipenv run autopep8 -d -a -r --max-line-length 140 --exit-code .
pipenv run black -l 140 --check .
