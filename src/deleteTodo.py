import json
import boto3
import os
import botocore

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def delete_todo(event, context):
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]
    todo_id = event["pathParameters"]["todoid"]

    try:
        table.delete_item(Key={"userid": user_id, "todoid": todo_id})
    except botocore.exceptions.ClientError as e:
        print(e)
        raise e
    except botocore.exceptions.ParamValidationError as e:
        raise ValueError('The parameters you provided are incorrect: {}'.format(e))
    
    return {"statusCode": 200, "body": json.dumps({"userid": user_id, "todoid": todo_id}),'headers': {"Access-Control-Allow-Origin": "*"}}