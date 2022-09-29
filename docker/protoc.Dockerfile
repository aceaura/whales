FROM ubuntu:20.04

ARG VERSION=v3.12.4

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