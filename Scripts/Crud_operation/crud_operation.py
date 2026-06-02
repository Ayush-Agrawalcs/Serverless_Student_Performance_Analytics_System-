import boto3
from decimal import Decimal

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('student_performance')

def new_student_record(id,hour,att,cl,total,gr,grade):
    table.put_item(
    Item={
        'student_id': id,
        'weekly_self_study_hours': Decimal(hour),
        'attendance_percentage': Decimal(att),
        'class_participation': Decimal(cl),
        'total_score': Decimal(total),
        'performance_category':gr,
        'grade': grade,
    }
    )
    print("Student record inserted successfully.")

def read_data(id):
    res=table.get_item(
        Key={
            'student_id': id
        }
    )
    print(res.get('Item'))

def update_data(student_id, field_name, value):

    table.update_item(
        Key={
            'student_id': student_id
        },
        UpdateExpression=f"SET {field_name} = :v",
        ExpressionAttributeValues={
            ':v': value
        }
    )

    print("Record updated successfully")

def delete_item(id):
    res=table.delete_item(
        Key={
            'student_id':id
        }
    )
    print("Deleteted")


