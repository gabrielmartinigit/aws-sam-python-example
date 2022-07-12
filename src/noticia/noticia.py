import os
from datetime import datetime
import uuid
import boto3
import json

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

events_client = boto3.client("events")


class Noticia:
    def __init__(self, id=None):
        self.id = id if id else str(uuid.uuid4())
        self.content = ""
        self.date = datetime.today().strftime('%Y-%m-%d')

    def upload_noticia(self):
        events_client.put_events(
            Entries=[
                {
                    'Source': 'contents.noticia',
                    'DetailType': 'Nova noticia',
                    'Detail': json.dumps({
                        "state": "created",
                        "id": self.id,
                        "content": self.content
                    })
                }
            ]
        )
        return "upload"

    def consultar_noticia(self):
        return "consultar"

    def listar_noticias(self):
        response = contents_table.scan()

        return response['Items']

    def store_noticia(self):
        contents_table.put_item(
            Item={
                'Id': self.id,
                'Content': self.content
            }
        )
