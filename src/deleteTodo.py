import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def delete_todo(event, context):
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
    todo_id = event["pathParameters"]["todoid"]

    table.delete_item(Key={"userid": user_id, "todoid": todo_id})
    
    return {"statusCode": 200, "body": json.dumps({"userid": user_id, "todoid": todo_id}),'headers': {"Access-Control-Allow-Origin": "*"}}