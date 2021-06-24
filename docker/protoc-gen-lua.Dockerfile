FROM python:2.7

COPY script/protoc-gen-lua /protoc-gen-lua
RUN ln -sf /protoc-gen-lua/bin/* /usr/local/bin/
RUN pip install -r /protoc-gen-lua/python/requirements.txt

ENTRYPOINT ["entrypoint.sh"]