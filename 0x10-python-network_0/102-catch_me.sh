#!/bin/bash
# Send Header
curl -s "$1" -sLH "X-HolbertonSchool-User-Id:98" -X POST -d "name=You got me!"
