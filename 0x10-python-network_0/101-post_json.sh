#!/bin/bash
# get status code
curl -X POST -H "Content-Type: application/json" -d"@$2" "$1"
