FROM ubuntu:20.04

ARG VERSION=main

RUN \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install autoconf automake libtool curl make g++ unzip git -y && \
    git clone -b ${VERSION} https://github.com/google/protobuf.git && \
    cd protobuf && \
    git submodule update --init --recursive && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

ENTRYPOINT [ "protoc" ]