import boto3
import botocore
import os
BUCKET = "bd-mindbenders12345"
s3 = boto3.client('s3')
s3.put_object(Bucket=BUCKET, Key="folder0/HappyFace.jpg", Body = b'HappyFace.jpg')
