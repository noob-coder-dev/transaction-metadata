#!/usr/bin/env bash
set -euo pipefail

rm -rf dist build
python -m build
python -m twine upload dist/*
