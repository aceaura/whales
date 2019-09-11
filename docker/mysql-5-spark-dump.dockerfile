FROM bde2020/spark-base:2.4.1-hadoop2.7

ENV MYSQL_HOST=0.0.0.0 \
    MYSQL_PORT=3306 \
    MYSQL_USER=root \
    MYSQL_PASSWORD=root \
    OUTPUT_DIR=/mysql-dump \
    WORK_DIR=/mysql-dump \
    PYSPARK_PYTHON=/usr/bin/python3

WORKDIR /

COPY /script/mysql-5-spark-dump-entrypoint.py /script/mysql-5-spark-dump-runner.py /script/

ENTRYPOINT ["/usr/bin/python3", "/script/mysql-5-spark-dump-entrypoint.py"]