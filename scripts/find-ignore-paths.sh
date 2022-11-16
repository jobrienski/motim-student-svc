#!/usr/bin/env bash
set -euo pipefail

# File to be sourced by other scripts who use the find command

# shellcheck disable=SC2034 # Other scripts source this file and use IGNORE_PATHS
IGNORE_PATHS=(\( \
    -path "*/.idea/*" -o \
    -path "*/.vscode/*" -o \
    -path "*/.pytest_cache/*" -o \
    -path "*/vendor/*" -o \
    -path "*/node_modules/*" -o \
    -path "*/.terraform/*" -o \
    -path "*/kubeconfig/*" -o \
    -path "*/terraform/environments/config/helm/*" -o \
    -path "*/.venv/*" -o \
    -path "*/dist/*" -o \
    -path "*/docker-cache/*" -o \
    -path "*/api.generated.*" \
\) -prune -o)
