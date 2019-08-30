FROM centos:7

ENV rvm_bin_path "/usr/local/rvm/bin"
ENV rvm_path "/usr/local/rvm"
ENV rvm_prefix "/usr/local"
ENV PATH "${PATH}:/usr/local/rvm/bin"
ENV rvm_version "1.29.9 (latest)"

RUN \
    yum -y install gcc automake autoconf libtool make which && \
    curl -sSL https://rvm.io/mpapis.asc | gpg --import - && \
    gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 39499BDB && \
    curl -L get.rvm.io | bash -s stable && \
    rvm install 2.3.3 && \
    rvm use 2.3.3 --default && \
    gem install redis-dump -V