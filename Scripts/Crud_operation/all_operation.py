import boto3
from boto3.dynamodb.conditions import Attr
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student_performance')

class All_operation:

    def Retrieve_based_on_attendance_percentage(self):

        print("read")

        res = table.scan(
            FilterExpression=Attr('attendance_percentage').gt(
                Decimal('90')
            )
        )

        for item in res['Items']:
            print(item)

    def Retrieve_based_on_weely_hour(self):

        print("read week")

        res = table.scan(
            FilterExpression=Attr('weekly_self_study_hours').gt(
                Decimal('10')
            )
        )

        for item in res['Items']:
            print(item)

    def Retrieve_based_on_performance(self):

        print("read performance")

        res = table.scan(
            FilterExpression=Attr('performance_category').eq(
                'Excellent'
            )
        )

        for item in res['Items']:
            print(item)