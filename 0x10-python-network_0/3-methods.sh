#!/bin/bash
# Options
curl -s -X OPTIONS "$1" -i | grep Allow | cut -c 8-
