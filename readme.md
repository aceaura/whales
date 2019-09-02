# redis 数据导入导出
注意：这里的ip必须使用docker host的内网和外网地址，不可以使用localhost或者127.0.0.1，这都是容器内部的地址。
## 导入
```shell
docker run --rm lizongti/docker-tools:redis-dump -u 192.168.0.1 > redis-data
```

## 导出
```shell
cat redis-data | docker run --rm -i lizongti/docker-tools:redis-load -u 192.168.0.1
```

## 管道传输
```shell
docker run --rm lizongti/docker-tools:redis-dump -u 192.168.0.1:6379 | docker run --rm -i lizongti/docker-tools:redis-load -u 192.168.0.1:6380
```
