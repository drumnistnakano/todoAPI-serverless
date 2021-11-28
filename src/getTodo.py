import json
import boto3
from boto3.dynamodb.conditions import Key
import os
import botocore

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

def get_todo(event, context):
    user_id = event["requestContext"]["authorizer"]["claims"]["sub"]

    try:
        if event["pathParameters"] is None:
            # クエリ文字列がない場合、ユーザの全てのTodoを取得
            result = table.query(KeyConditionExpression=Key("userid").eq(user_id))
            item = result.get('Items')
        else:
            # クエリ文字列がある場合、ユーザの単一のTodoを取得
            result = table.get_item(Key={"userid": user_id, "todoid": event["pathParameters"]["todoid"]})
            item = result.get('Item')
    except botocore.exceptions.ClientError as e:
        print(e)
        raise e
    except botocore.exceptions.ParamValidationError as e:
        raise ValueError('The parameters you provided are incorrect: {}'.format(e))

    print(item)
    return {"statusCode": 200, "body": json.dumps(item),'headers': {"Access-Control-Allow-Origin": "*"}}