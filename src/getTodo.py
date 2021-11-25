import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def get_todo(event, context):
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]

    if event["pathParameters"] is None:
        allusers_todo = table.query(KeyConditionExpression=Key("userid").eq(user_id))
        item = allusers_todo.get("Items")
    else:
        todo = table.get_item(Key={"userid": user_id, "todoid": event["pathParameters"]["todoid"]})
        item = todo.get("Item")

    return {"statusCode": 200, "body": json.dumps(item)}