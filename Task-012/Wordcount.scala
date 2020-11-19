import org.apache.spark._


object WordCount {
	def main(args: Array[String]) {
		val conf = new SparkConf().setAppName("wordcount").setMaster("local[*]")
		// Create a Scala Spark Context.
		val sc = new SparkContext(conf)
		// Load our input data.
		val input = sc.textFile("/home/field/Shakespeare.txt")
		// Split up into words.
		val words = input.flatMap(line => line.split(" "))
		// Transform into word and count.
		val counts = words.map(word => (word, 1)).reduceByKey { case (x, y) => x + y }
		// Save the word count back out to a text file, causing evaluation.
		counts.saveAsTextFile("/home/field/Shakespeare_output_scala")
		sc.stop()
  }
}
