import boto3
from dotenv import load_dotenv
import os
load_dotenv()

s3=boto3.client('s3')
file_path = "../../data/data1.csv"
file_path1="../../data/student_data.csv"
file_path2="../../data/student_data.json"
bucketName=os.getenv('bucket_name')
s3_key=os.getenv('s3_keys')
s3_keys=os.getenv('s3_k')
s3_k=os.getenv('s3_ke')
# s3.upload_file(file_path, bucketName, s3_key)
s3.upload_file(file_path1, bucketName, s3_keys)
s3.upload_file(file_path2, bucketName, s3_keys)
print("File uploaded successfully")