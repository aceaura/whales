FROM centos:7

RUN \
    yum groupinstall -y "Development tools" && \
    yum install -y  wget zlib-devel curl-devel openssl-devel httpd-devel apr-devel apr-util-devel mysql-devel && \
    wget https://cache.ruby-lang.org/pub/ruby/2.6/ruby-2.6.4.tar.gz && tar xf ruby-2.6.4.tar.gz && cd ruby-2.6.4 && ./configure && make install && cd .. && rm -rf ruby-2.6.4* && \
    gem install redis-dump -V

ENTRYPOINT ["redis-dump"]