from pyspark.sql import SparkSession
from pyspark import SparkConf
import sys

spark = SparkSession.builder.config(conf = SparkConf()).getOrCreate()

from mysql_5_dump_mapper import main as map
spark.read.jdbc(
    url = sys.argv[1], table = sys.argv[2], properties = {"driver": "com.mysql.jdbc.Driver"}
).rdd.repartition(int(sys.argv[3])).map(map).repartition(1).saveAsTextFile(sys.argv[4])
spark.stop()
