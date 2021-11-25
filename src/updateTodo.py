import json
import boto3
import base64

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def update_todo(event, context):
    user_id = event["pathParameters"]["userId"]
    body = json.loads(event.get("body"))
    todo_id = body.get("todoId")
    title = body.get("title")
    content = body.get("content")
    
    item = {"userId": user_id, "todoId": todo_id, "title": title, "content": content}

    table.update_item(
        Key={"userId": user_id, "todoId": todo_id},
        UpdateExpression="set title=:title, content=:content",
        ExpressionAttributeValues={":title": title, ":content": content}
    )

    return {"statusCode": 200, "body": json.dumps(item)}
