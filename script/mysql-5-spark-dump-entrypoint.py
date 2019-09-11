from pyspark.sql import SparkSession
from pyspark import SparkConf
import os, sys, time, importlib, multiprocessing
sys.path.append("/" if "WORK_DIR" not in os.environ else os.environ["WORK_DIR"])

mysql_host = "localhost" if "MYSQL_HOST" not in os.environ else os.environ["MYSQL_HOST"]
mysql_port = 3306 if "MYSQL_PORT" not in os.environ else int(os.environ["MYSQL_PORT"])
mysql_user = "root" if "MYSQL_USER" not in os.environ else os.environ["MYSQL_USER"]
mysql_password = "root" if "MYSQL_PASSWORD" not in os.environ else os.environ["MYSQL_PASSWORD"]
url = "jdbc:mysql://{}:{}?user={}&password={}".format(mysql_host, mysql_port, mysql_user, mysql_password)
table = sys.argv[1]
properties={"driver": "com.mysql.jdbc.Driver"}
cpu_count = multiprocessing.cpu_count()
map = importlib.import_module(sys.argv[2]).map
output_dir = "{}/{}/{}".format("/" if "OUTPUT_DIR" not in os.environ else os.environ["OUTPUT_DIR"], table, time.time()) 

spark = SparkSession.builder.config(conf = SparkConf()).getOrCreate()
spark.read.jdbc(
    url = url, table = table, properties = properties
).rdd.repartition(cpu_count).map(map).repartition(1).saveAsTextFile(output_dir)
spark.stop()
