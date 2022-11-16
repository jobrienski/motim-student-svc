#!/usr/bin/env bash
set -euo pipefail

echo "Running 'standard auditor'"

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

"$DIR/echo-error.sh" snyk test
