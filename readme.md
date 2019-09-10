# redis 数据导入导出
注意：这里的ip必须使用docker host的内网和外网地址，不可以使用localhost或者127.0.0.1，这都是容器内部的地址。
## 导出
```shell
docker run --rm lizongti/docker-tools:redis-dump -u 192.168.0.1 > redis-data
```

## 导入
```shell
cat redis-data | docker run --rm -i lizongti/docker-tools:redis-load -u 192.168.0.1
```

## 管道传输
```shell
docker run --rm lizongti/docker-tools:redis-dump -u 192.168.0.1:6379 | docker run --rm -i lizongti/docker-tools:redis-load -u 192.168.0.1:6380
```

# mysql 数据导入导出
注意：这里的ip必须使用docker host的内网和外网地址，不可以使用localhost或者127.0.0.1，这都是容器内部的地址。
## 导出
```shell
# 导出数据和结构
docker run -e MYSQL_PWD=root --rm lizongti/docker-tools:mysql-dump -h192.168.0.1 -P3306 -uroot --databases db1 db2 > mysql-data
# 导出数据
docker run -e MYSQL_PWD=root --rm lizongti/docker-tools:mysql-dump --no-create-info -h192.168.0.1 -P3306 -uroot --databases db1 db2 > mysql-data
# 导出结构
docker run -e MYSQL_PWD=root --rm lizongti/docker-tools:mysql-dump --no-data -h192.168.0.1 -P3306 -uroot --databases db1 db2 > mysql-data
```
其他参数
```c
--no-create-db，  ---取消创建数据库sql(默认存在)
--no-create-info，---取消创建表sql(默认存在)
--no-data         ---不导出数据(默认导出)
--add-drop-database ---增加删除数据库sql（默认不存在）
--skip-add-drop-table  ---取消每个数据表创建之前添加drop数据表语句(默认每个表之前存在drop语句)
--skip-add-locks       ---取消在每个表导出之前增加LOCK TABLES（默认存在锁）
--skip-comments        ---注释信息(默认存在)
```
## 导入
```shell
cat mysql-data | docker run -e MYSQL_PWD=root --rm lizongti/docker-tools:mysql-load -h192.168.0.1 -P3306 -uroot 
```

## 管道传输
docker run -e MYSQL_PWD=root --rm lizongti/docker-tools:mysql-dump -h192.168.0.1 -P3306 -uroot --databases db1 db2 | docker run -e MYSQL_PWD=root --rm lizongti/docker-tools:mysql-load -h192.168.0.1 -P3307 -uroot 
