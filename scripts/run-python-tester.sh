#!/usr/bin/env bash
set -euo pipefail

ENVIRONMENT="testing" pipenv run pytest -s .
