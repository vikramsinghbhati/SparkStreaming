from pyspark.sql import SparkSession
from StreamingIntro.commonFunc import read_schema
import configparser


spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext

#SparkSession.builder.config(conf=SparkConf())
#spark=SparkSession.Builder.getOrCreate()

#reading all config like schema and input path
config=configparser.ConfigParser()
config.read(r"C:\Users\91988\Desktop\Pyspark_practice\SparkStreaming\StreamingIntro\ProjectConfig\config.ini")
inputpath=config.get('paths','inputLocation')
inputschemafromconfig=config.get('Schema','landingFileSchema')
inputschema=read_schema(inputschemafromconfig)

#creating datafrme with these schema and inputpath
inputDF=spark.readStream.format("csv").option("header",False).schema(inputschema).load(inputpath)
#inputDF.show()

#printing the DF output of input location data into console
inputDF.writeStream.format('console').outputMode('append').start().awaitTermination()





