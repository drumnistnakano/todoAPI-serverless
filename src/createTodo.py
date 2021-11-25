import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def create_todo(event, context):
    body = json.loads(event.get("body"))
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
    todo_id = body.get("todoId") 
    title = body.get("title")
    content = body.get("content")

    item = {"userId": user_id, "todoId": todo_id, "title": title, "content": content}
    
    table.put_item(Item=item)

    return {"statusCode": 200, "body": json.dumps(item)}
