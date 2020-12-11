import boto3
import botocore
import os
BUCKET = "bd-mindbenders12345"

s3 = boto3.client('s3')
s3s= boto3.resource('s3')

s3.put_object(Bucket=BUCKET, Key="HappyFace.jpg", Body = 'HappyFace.jpg')

obj = s3s.Object("bd-mindbenders12345", "HappyFace.jpg")
body = obj.get()['Body'].read()
