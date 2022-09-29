#!/bin/bash

rm -rf ./github/workflows/* && \
find ./docker -name "*.Dockerfile" | \
awk -F '[/|.]' '{print $4}'| \
xargs -I {} \
env "$(echo 'tag={}')" \
env "$(echo 'username={{ secrets.DOCKERHUB_USERNAME }}')" \
env "$(echo 'password={{ secrets.DOCKERHUB_TOKEN }}')" \
gomplate -f ./template/workflow.template.yml -o ./.github/workflows/{}.yml

