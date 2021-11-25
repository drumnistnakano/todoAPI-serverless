import json
import boto3
import base64

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def delete_todo(event, context):
    user_id = event["pathParameters"]["userId"]
    body = json.loads(event.get("body"))
    todo_id = body.get("todoId")

    table.delete_item(Key={"userId": user_id, "todoId": todo_id})
    
    return {"statusCode": 200, "body": json.dumps({"userId": user_id, "todoId": todo_id})}