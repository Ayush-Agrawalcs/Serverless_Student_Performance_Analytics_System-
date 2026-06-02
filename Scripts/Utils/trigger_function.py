import csv
import boto3
from decimal import Decimal
import io

s3=boto3.client('s3')
dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('student_performance')

def lambda_handler(event,context):
    print("Function Ran!!")
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    print(bucket)
    print(key)
    obj=s3.get_object(Bucket=bucket, Key=key)
    print("File fetched")
    line=io.TextIOWrapper(obj['Body'], encoding='utf-8')
    print("CSV loaded")
    reader=csv.DictReader(line)
    for row in reader:
        print("Processing:", row)
        total_score=Decimal(row['total_score']).quantize(Decimal('0.00'))

        if total_score>=Decimal('90.00'):
            performance_category="Excellent"
        elif total_score>=Decimal('75.00'):
            performance_category="Good"
        elif total_score>=Decimal('60.00'):
            performance_category="Average"
        else:
            performance_category="Poor"

        table.put_item(
            Item={'student_id': int(row['student_id']),
                    'weekly_self_study_hours': Decimal(row['weekly_self_study_hours']).quantize(Decimal('0.00')),
                    'attendance_percentage': Decimal(row['attendance_percentage']).quantize(Decimal('0.00')),
                    'class_participation': Decimal(row['class_participation']).quantize(Decimal('0.00')),
                    'total_score': total_score,
                    'grade': row['grade'],
                    'performance_category':performance_category
            }
        )
    return {
        'statusCode': 200,
        'message': 'CSV processed successfully'
    }
    
