#!/bin/bash
# Send Header
curl -s "$1" -H "X-HolbertonSchool-User-Id:98" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
