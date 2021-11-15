import json
import random
import boto3
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def delete_todo(event, context):
    id = event["pathParameters"]["id"]
    table.delete_item(Key={"id": id})
    response = {"statusCode": 200, "body": json.dumps({"id": id})}
    return response
