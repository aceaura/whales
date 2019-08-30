FROM centos:7

RUN \
    yum -y install gcc automake autoconf libtool make && \
    curl -sSL https://rvm.io/mpapis.asc | gpg --import - && \
    gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 39499BDB && \
    curl -L get.rvm.io | bash -s stable && \
    source /etc/profile && \
    rvm install 2.3.3 && \
    rvm use 2.3.3 --default && \
    gem install redis-dump -V