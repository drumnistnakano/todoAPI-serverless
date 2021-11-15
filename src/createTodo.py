import json
import random
import boto3
import string

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('TodoTable')

def create_todo(event, context):
    body = json.loads(event.get("body"))
    title = body.get("title")
    content = body.get("content")
    id = "".join(random.choices(string.ascii_letters + string.digits, k=12))
    item = {"id": id, "title": title, "content": content}
    table.put_item(Item=item)
    response = {"statusCode": 200, "body": json.dumps(item)}
    return response
