FROM python:2.7

COPY script/protoc-gen-lua/protoc script/protoc-gen-lua/protoc-gen-lua script/protoc-gen-lua/plugin_pb2.py script/protoc-gen-lua/entrypoint.sh /usr/local/bin/
COPY script/protoc-gen-lua/requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

ENTRYPOINT ["entrypoint.sh"]