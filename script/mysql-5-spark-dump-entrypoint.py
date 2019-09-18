#!/usr/bin/python3
import os, sys, time, multiprocessing

mysql_host = "localhost" if "MYSQL_HOST" not in os.environ else os.environ["MYSQL_HOST"]
mysql_port = 3306 if "MYSQL_PORT" not in os.environ else int(os.environ["MYSQL_PORT"])
mysql_user = "root" if "MYSQL_USER" not in os.environ else os.environ["MYSQL_USER"]
mysql_password = "root" if "MYSQL_PASSWORD" not in os.environ else os.environ["MYSQL_PASSWORD"]
jdbc_url = "jdbc:mysql://{}:{}?user={}&password={}".format(mysql_host, mysql_port, mysql_user, mysql_password)
work_dir = "/work" if "WORK_DIR" not in os.environ else os.environ["WORK_DIR"]
output_dir = "{}/{}".format("/output" if "OUTPUT_DIR" not in os.environ else os.environ["OUTPUT_DIR"], sys.argv[1])
execute_repartition = multiprocessing.cpu_count() if "EXECUTE_REPARTITION" not in os.environ else int(os.environ["EXECUTE_REPARTITION"])
result_repartition = multiprocessing.cpu_count() if "RESULT_REPARTITION" not in os.environ else int(os.environ["RESULT_REPARTITION"])
spark_args = "" if "SPARK_ARGS" not in os.environ else os.environ["SPARK_ARGS"]
table_name = sys.argv[1]

commands = [
    "mkdir /mysql-dump-run/ && cp -rf /script/mysql-5-spark-dump-runner.py /mysql-dump-run/ && cp -rf {}/* /mysql-dump-run/".format(work_dir),
    "mv /mysql-dump-run/{}.py /mysql-dump-run/mysql_5_dump_mapper.py".format(sys.argv[2]),
    "rm -rf {}".format(output_dir),
    "cd /mysql-dump-run/ && /spark/bin/spark-submit --packages=mysql:mysql-connector-java:5.1.48 {} mysql-5-spark-dump-runner.py '{}' '{}' '{}' '{}' '{}'".format(spark_args, jdbc_url, table_name, execute_repartition, result_repartition, output_dir)
]
for command in commands:
    print("OS Execute: {}".format(command))

for command in commands:
    os.system(command)