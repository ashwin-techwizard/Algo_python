# from pyspark.sql import SparkSession
# #import pyspark.sql
# spark = SparkSession.builder.appName("missingdata").getOrCreate()


import isodate
from pyspark.sql import SparkSession
# from pyspark.sql.functions import col, when
import pyspark.sql.functions as Fn
# Spark session & context
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.master('local').getOrCreate()
sc = spark.sparkContext

peopleDF = spark.read.json("D:\Work\PythonWorkSpace\RecipeAnalytics\input\recipes.json")
peopleDF.withColumn("ingredientsMM" ,Fn.split(Fn.col('ingredients'), "\n"))

peopleDF.show()
#
# training_df = spark.read.json('recipes.json')
#
# def isoTimeToMin(iso_str):
#      return (isodate.parse_duration(iso_str).seconds % 3600) // 60
#
# isoTimeToMin_UDF = Fn.udf(isoTimeToMin, IntegerType())
# transformed =training_df.withColumn("ingredientsMM" ,Fn.split(Fn.col('ingredients'), "\n"))\
# .withColumn("cookTimeProcessed", isoTimeToMin_UDF(training_df['cookTime']))\
# .withColumn("prepTimeProcessed", isoTimeToMin_UDF(training_df['prepTime']))\
#     .withColumn("total_cook_time", isoTimeToMin_UDF(training_df['cookTime'] ) +isoTimeToMin_UDF(training_df['prepTime']))
#
# from pyspark import SparkConf
# from pyspark import SparkContext
#
# conf = SparkConf()
# conf.setMaster('spark://HEAD_NODE_HOSTNAME:7077')
# conf.setAppName('spark-basic')
# sc = SparkContext(conf=conf)
#
# def mod(x):
#     import numpy as np
#     return (x, np.mod(x, 2))
#
# rdd = sc.parallelize(range(1000)).map(mod).take(10)
#
#
# lyrics = sc.textFile("https://s3-eu-west-1.amazonaws.com/dwh-test-resources/recipes.json")
