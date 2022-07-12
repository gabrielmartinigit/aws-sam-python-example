import os
import json
import boto3

aws_environment = os.environ['AWSENV']
table_name = os.environ['TABLE']

# Check if executing locally or on AWS, and configure DynamoDB connection accordingly
if aws_environment == "AWS_SAM_LOCAL":
    # SAM LOCAL
    contents_table = boto3.resource(
        'dynamodb',
        endpoint_url="http://127.0.0.1:8000").Table(table_name)
else:
    # AWS
    contents_table = boto3.resource(
        'dynamodb').Table(table_name)

s3_client = boto3.client("s3")


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "receita",
            "env": f"{aws_environment}",
            "connection": f"{contents_table}"
        }),
    }
