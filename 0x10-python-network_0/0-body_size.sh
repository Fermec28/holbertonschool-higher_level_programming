#!/bin/bash
# get the Content-length
curl -s "$1" | wc -c
