import pydoop.hdfs as hdfs
import boto3
import botocore

s3 = boto3.resource('s3')

BUCKET = "bd-mindbenders12345"

file = hdfs.open("hdfs://localhost:9000/test.txt")

s3.Bucket(BUCKET).put_object(Key="test.txt", Body=file)         
