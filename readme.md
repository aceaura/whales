# redis 数据导入导出

## 导入
```shell
docker run --rm lizongti/docker-tools:redis-dump -u localhost > redis-data
```

## 导出
```shell
cat redis-data | docker run --rm -i lizongti/docker-tools:redis-load -u localhost
```

## 管道传输
```shell
docker run --rm lizongti/docker-tools:redis-dump -u localhost:6379 | docker run --rm -i lizongti/docker-tools:redis-load -u localhost:6380
```
