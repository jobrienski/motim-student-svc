#!/usr/bin/env bash
set -euo pipefail

pipenv run autopep8 -i -a -r --max-line-length 140 .
pipenv run black -l 140 .
