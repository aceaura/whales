#!/bin/bash
find ./docker -name "*.Dockerfile" | \
awk -F '[/|.]' '{print $4}'| \
xargs -I {} \
./tag.sh {}