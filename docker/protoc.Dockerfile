FROM ubuntu:latest

ARG VERSION=main

RUN \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install autoconf automake libtool curl make g++ unzip git -y && \
    git clone https://github.com/google/protobuf.git@latest && \
    cd protobuf && \
    git checkout ${VERSION} && \
    git submodule update --init --recursive && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

ENTRYPOINT [ "protoc" ]