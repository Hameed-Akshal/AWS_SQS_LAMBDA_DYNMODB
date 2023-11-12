import json
import boto3

# Initialize SQS and DynamoDB clients
sqs = boto3.client('sqs', region_name='your-region')  # Replace 'your-region' with your AWS region
dynamo_db = boto3.resource('dynamodb', region_name='your-region')  # Replace 'your-region' with your AWS region
table = dynamo_db.Table('your-dynamodb-table')  # Replace 'your-dynamodb-table' with your DynamoDB table name

def lambda_handler(event, context):
    try:
        # Process SQS messages
        for record in event['Records']:
            # Parse the message into a JSON object
            body = json.loads(record['body'])
            
            # Log the body, which is the message
            print("Incoming message body from SQS:", body)

            # Define the item to be written to DynamoDB
            item = {
                'userId': body['userId'],
                'name': body['name'],
                'age': body['age']
            }

            # Write data to DynamoDB
            table.put_item(Item=item)

            print('Successfully written to DynamoDB')

    except Exception as e:
        print('Error in executing lambda:', str(e))
        return {"statusCode": 500, "message": "Error while execution"}

# Uncomment the next line if you want to test the Lambda function locally
# lambda_handler({"Records": [{"body": '{"userId": "123", "name": "John", "age": 30}'}]}, None)
