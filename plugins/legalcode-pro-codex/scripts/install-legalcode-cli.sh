#!/usr/bin/env bash
set -euo pipefail

if ! command -v npm >/dev/null 2>&1; then
  echo "npm is required to install the Legalcode CLI." >&2
  exit 1
fi

npm install -g legalcode
legalcode --help
