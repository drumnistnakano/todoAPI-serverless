import json
import boto3
import base64

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def create_todo(event, context):
    decoded_body = base64.b64decode(event.get("body")).decode()
    body = json.loads(decoded_body)

    user_id = body.get("userId") 
    todo_id = body.get("todoId") 
    title = body.get("title")
    content = body.get("content")

    item = {"userId": user_id, "todoId": todo_id, "title": title, "content": content}

    table.put_item(Item=item)
    
    return {"statusCode": 200, "body": json.dumps(item)}
