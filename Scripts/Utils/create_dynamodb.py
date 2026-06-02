import boto3

dynamodb=boto3.client('dynamodb')

table=dynamodb.create_table(
    TableName="student_performance",
    KeySchema=[
        {
            'AttributeName':'student_id',
            'KeyType':'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName':'student_id',
            'AttributeType':'N'
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)
print("Creating table...")
table.wait_until_exists()
print("Table status:",table.table_status)