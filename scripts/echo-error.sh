#!/usr/bin/env bash
set -uo pipefail

# This script wraps a command, outputting the results only if the command fails

echo "Running: $*"
output="$("$@")"
ec=$?

if [[ $ec -ne 0 ]] ; then
  echo "$output"
  exit $ec
else
  echo "Success!"
fi
