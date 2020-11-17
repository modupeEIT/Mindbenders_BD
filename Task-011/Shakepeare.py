from pyspark import SparkContext
from pyspark import SparkConf

# create Spark context with Spark configuration
conf = SparkConf().setAppName("Shakespeare")
sc = SparkContext(conf=conf)


# read data from text file and split each line into words
words = sc.textFile("/home/field/Shakespeare.txt").flatMap(lambda line: line.split(" "))
	
# count the occurrence of each word
wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)

# save the counts to output
wordCounts.saveAsTextFile("/home/field/Shakespeare_output")


