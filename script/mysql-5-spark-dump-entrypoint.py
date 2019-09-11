from pyspark.sql import SparkSession
from pyspark import SparkConf
import os, sys, time, importlib, multiprocessing

work_dir = "/" if "WORK_DIR" not in os.environ else os.environ["WORK_DIR"]
sys.path.append(work_dir)
print("Work directory is set as {}".format(work_dir))

mysql_host = "localhost" if "MYSQL_HOST" not in os.environ else os.environ["MYSQL_HOST"]
mysql_port = 3306 if "MYSQL_PORT" not in os.environ else int(os.environ["MYSQL_PORT"])
mysql_user = "root" if "MYSQL_USER" not in os.environ else os.environ["MYSQL_USER"]
mysql_password = "root" if "MYSQL_PASSWORD" not in os.environ else os.environ["MYSQL_PASSWORD"]
url = "jdbc:mysql://{}:{}?user={}&password={}".format(mysql_host, mysql_port, mysql_user, mysql_password)
print("JDBC url is set as {}".format(url))

table = sys.argv[1]
print("Table name is set as {}", table)

properties={"driver": "com.mysql.jdbc.Driver"}
map = importlib.import_module(sys.argv[2]).map
output_dir = "{}/{}/{}".format("/" if "OUTPUT_DIR" not in os.environ else os.environ["OUTPUT_DIR"], table, time.time()) 
print("Output Directory is set as {}".format(output_dir))

cpu_count = multiprocessing.cpu_count()
print("Repatitions is set as {}".format(cpu_count))

spark = SparkSession.builder.config(conf = SparkConf()).getOrCreate()
spark.read.jdbc(
    url = url, table = table, properties = properties
).rdd.repartition(cpu_count).map(map).repartition(1).saveAsTextFile(output_dir)
spark.stop()
