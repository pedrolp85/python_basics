#!/bin/bash

set -ex

isort --check-only .
black . --check
flake8 .
vulture . --min-confidence 70
mypy .
