import json
import boto3
import os
import botocore

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def create_todo(event, context):
    body = json.loads(event.get("body"))
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
    todo_id = body.get("todoid") 
    title = body.get("title")
    content = body.get("content")

    item = {"userid": user_id, "todoid": todo_id, "title": title, "content": content}
    
    try:
        table.put_item(Item=item)
    except botocore.exceptions.ClientError as e:
        print(e)
        raise e
    except botocore.exceptions.ParamValidationError as e:
        raise ValueError('The parameters you provided are incorrect: {}'.format(e))
    
    return {"statusCode": 200, "body": json.dumps(item), 'headers': {"Access-Control-Allow-Origin": "*"}}
