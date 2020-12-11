import boto3
import botocore
import os

s3 = boto3.client('s3')
s3s = boto3.resource('s3')

s3s.create_bucket(Bucket="bucket-eit-dupe001", CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

s3.put_object(Bucket="bucket-eit-dupe001", Key="bigdata-eit02/HappyFace.jpg", Body = 'HappyFace.jpg')
