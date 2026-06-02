import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('student_performance')


class SecondaryIndexOperations:

    # Top Students in Grade A
    def top_students_grade_a(self):

        response = table.query(
            IndexName='GradeScoreIndex',
            KeyConditionExpression=Key('grade').eq('A'),
            ScanIndexForward=False,
            Limit=10
        )

        print("\nTop Students in Grade A\n")

        for item in response['Items']:
            print(item)

    # Students with Highest Scores Overall
    def highest_scores(self):

        response = table.scan()

        students = response['Items']

        students = sorted(
            students,
            key=lambda x: float(x['total_score']),
            reverse=True
        )

        print("\nTop 10 Students Overall\n")

        for student in students[:10]:
            print(student)