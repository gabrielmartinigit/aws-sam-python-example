# AWS Event-Driven Architecture (EDA) SAM sample

## Architecture

![Architecture](./images/EDA.jpg)

## Getting Started

```bash
    sam init # start sam project
    sam validate
    sam build
    sam local invoke HelloWorldFunction --event events/hello_world_event.json
    sam local start-api --env-vars env.json
    sam deploy --stack-name aws-sam-python-example --resolve-s3 --capabilities CAPABILITY_IAM
    sam delete --stack-name aws-sam-python-example
```

```bash
    docker run -p 8000:8000 amazon/dynamodb-local
    aws dynamodb list-tables --endpoint-url http://localhost:8000
    aws dynamodb create-table --cli-input-json file://data_model/contents_table_model.json --endpoint-url http://localhost:8000
    aws dynamodb delete-table --table-name ContentsTable --endpoint-url http://localhost:8000
```
