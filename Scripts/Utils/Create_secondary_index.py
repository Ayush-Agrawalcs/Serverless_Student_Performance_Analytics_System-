import boto3

client = boto3.client('dynamodb')

response = client.update_table(
    TableName='student_performance',

    AttributeDefinitions=[
        {
            'AttributeName': 'grade',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'total_score',
            'AttributeType': 'N'
        }
    ],

    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'GradeScoreIndex',

                'KeySchema': [
                    {
                        'AttributeName': 'grade',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'total_score',
                        'KeyType': 'RANGE'
                    }
                ],

                'Projection': {
                    'ProjectionType': 'ALL'
                }
            }
        }
    ]
)

print("GSI Creation Started")