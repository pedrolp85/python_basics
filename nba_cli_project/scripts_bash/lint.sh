#!/bin/bash

set -ex

isort --check-only .
black . --check
