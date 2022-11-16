#!/usr/bin/env bash
set -euo pipefail

echo "Running 'python auditor'"

PIPENV_PYUP_API_KEY="" pipenv check
