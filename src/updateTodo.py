import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def update_todo(event, context):
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
    todo_id = event["pathParameters"]["todoid"]
    body = json.loads(event.get("body"))
    title = body.get("title")
    content = body.get("content")
    
    item = {"userid": user_id, "todoid": todo_id, "title": title, "content": content}

    table.update_item(
        Key={"userid": user_id, "todoid": todo_id},
        UpdateExpression="set title=:title, content=:content",
        ExpressionAttributeValues={":title": title, ":content": content}
    )

    return {"statusCode": 200, "body": json.dumps(item),'headers': {"Access-Control-Allow-Origin": "*"}}