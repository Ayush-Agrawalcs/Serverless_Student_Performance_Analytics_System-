import boto3
import os
from dotenv import load_dotenv
load_dotenv()

region='ap-south-1'
s3=boto3.client('s3',region_name=region)

s3.create_bucket(
    Bucket=os.getenv('bucket_name'),
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)