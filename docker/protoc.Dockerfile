FROM ubuntu:latest

ARG VERSION=master

RUN \
    apt-get update && \
    apt-get upgrade -y && \
    apt-get install autoconf automake libtool curl make g++ unzip git -y && \
    git clone -b main https://github.com/google/protobuf.git && \
    cd protobuf && \
    git checkout ${VERSION} && \
    git submodule update --init --recursive && \
    ./autogen.sh && \
    ./configure && \
    make && \
    make install && \
    ldconfig

ENTRYPOINT [ "protoc" ]