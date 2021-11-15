import json
import random
import boto3
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def get_todo(event, context):
    id = event["pathParameters"]["id"]
    res = table.get_item(Key={"id": id})
    item = res.get("Item")
    response = {"statusCode": 200, "body": json.dumps(item)}
    return response