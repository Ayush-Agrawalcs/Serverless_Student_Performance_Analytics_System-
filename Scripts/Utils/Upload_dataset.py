import boto3
from dotenv import load_dotenv
import os
load_dotenv()

s3=boto3.client('s3')
file_path = "../../data/data1.csv"
bucketName=os.getenv('bucket_name')
s3_key=os.getenv('s3_keys')
s3.upload_file(file_path, bucketName, s3_key)
print("File uploaded successfully")