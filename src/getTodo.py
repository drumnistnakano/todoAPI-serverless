import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def get_todo(event, context):
    user_id = event["pathParameters"]["userId"]

    res = table.query(KeyConditionExpression=Key("userId").eq(user_id))
    item = res.get("Items")

    return {"statusCode": 200, "body": json.dumps(item)}