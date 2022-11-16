#!/usr/bin/env bash
set -euo pipefail

# Ensures various files are formatted correctly

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# shellcheck source=scripts/find-ignore-paths.sh
source "$DIR/find-ignore-paths.sh"

find . "${IGNORE_PATHS[@]}" \( \
    -iname "*.yml" -o \
    -iname "*.yaml" -o \
    -iname "*.md" -o \
    -iname "*.graphql" -o \
    -iname "*.ts" -o \
    -iname "*.js" -o \
    -iname "*.json" -o \
    -iname "*.scss" -o \
    -iname "*.css" -o \
    -iname ".prettierrc" \
  \) \
  -exec prettier --write {} +
