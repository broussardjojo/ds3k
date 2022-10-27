#usr/bin/env bash
env $(grep -v '^#' .env | xargs)