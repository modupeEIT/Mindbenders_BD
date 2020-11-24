from pyspark import SparkContext 
from pyspark.sql import SQLContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from pyspark.sql import SparkSession
import pyspark.sql.types as st
from pyspark.sql.functions import col
import json



if __name__== "__main__":
    
    sc = SparkContext("local[*]", )
    ssc = StreamingContext(sc, 20)
    ss = SparkSession.builder \
        .appName("Stains") \
            .master("local[*]") \
                .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
                    .config("hive.metastore.uris", "thrift://localhost:9083") \
                        .enableHiveSupport().getOrCreate()
    

    kafkaStream = KafkaUtils.createStream(ssc, "localhost:2181","Strains", {"weeds1" : 1})

        # Parse the Tweets
    parsed = kafkaStream.map(lambda y:json.loads(y[1]))
    
            

    sch = st.StructType([st.StructField('desc', st.StringType(), True)])
    def process(rdd):
        if not rdd.isEmpty():
            global ss
            df = ss.createDataFrame(rdd, schema=sch)
            df.show()
            df.write.saveAsTable(name ="default.weeds", format="hive", mode="append")

        # Write parsed tweets to Hive
    parsed.foreachRDD(process)


    ssc.start()
    ssc.awaitTermination()
