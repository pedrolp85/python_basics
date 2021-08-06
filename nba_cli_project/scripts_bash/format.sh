#!/bin/bash

set -ex

isort .
black .
autoflake --recursive --remove-all-unused-imports --remove-unused-variables --in-place .