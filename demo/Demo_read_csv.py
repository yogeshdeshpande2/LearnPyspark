import findspark
findspark.init()

# Import required libraries
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("test").getOrCreate()

# Read the csv and print the spark dataframe
df = spark.read.option("header", True).csv('../data/employee_test.csv')
df.show()