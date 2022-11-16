#!/usr/bin/env bash
#set -euo pipefail

inside_docker() {
  grep -o -E '/docker/.+' < /proc/self/cgroup
}

if [ "${CI:-}" != "true" ]; then
  docker-compose up --detach postgres >/dev/null 2>&1
  sleep 2
  if inside_docker >/dev/null 2>&1 ; then
    echo "export POSTGRES_HOST=postgres"
    echo "export POSTGRES_PORT=5432"
  fi
fi
