import json
import random
import boto3
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def update_todo(event, context):
    id = event["pathParameters"]["id"]
    body = json.loads(event.get("body"))
    title = body.get("title")
    content = body.get("content")
    item = {"id": id, "title": title, "content": content}
    table.update_item(
        Key={"id": id},
        UpdateExpression="set todo=:todo",
        ExpressionAttributeValues={":todo": todo},
    )
    response = {"statusCode": 200, "body": json.dumps(item)}
    return response
