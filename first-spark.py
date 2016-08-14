from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)
obj = sc.textFile("temp.txt")
obj.filter(lambda line: len(line) > 10 )
print obj.first()
