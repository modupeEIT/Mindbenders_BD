import org.apache.spark._
import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType, DoubleType}
import org.apache.spark.sql.functions._
import org.apache.spark.sql._
import org.apache.spark.sql.streaming._

object KafkaConsumerApp{
	def main(args: Array[String]) {
		val spark = SparkSession.builder.appName("Kafka Consumer App").master("local[*]").getOrCreate()
		import spark.implicits._
		
		val inputDF = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "localhost:9092").option("subscribe", "stocks").option("startingOffsets", "earliest").load()


		val dataStruct = new StructType()		
					.add("datetime", StringType, true)
					.add("open", StringType, true)
					.add("high", StringType, true)
					.add("low", StringType, true)
					.add("close", StringType, true)
					.add("volume", StringType, true)
					
	
		val dataDF = inputDF.select($"value" cast "string" as "json").select(from_json($"json", dataStruct) as "data").select("data.*")
		
		val dataDF1 = dataDF.select("*")
		val rwDF = dataDF1.writeStream.outputMode("update").format("console").start()
		rwDF.awaitTermination()		
		dataDF.write.option("header","true").csv("hdfs://master:9000/user.txt")
	}
}



