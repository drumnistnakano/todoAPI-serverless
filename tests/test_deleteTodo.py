import boto3
import pytest
import os
import yaml
import json
from moto import mock_dynamodb2

@pytest.mark.parametrize(
    "event, expected",
    [
        (
            {
                "requestContext": {
                    "authorizer": {
                        "claims": {
                            "sub": "0001"
                        }
                    }
                },
                "pathParameters": {
                    "todoid": "0001"
                } 
            },
            {
                "statusCode": 200,
                "body": json.dumps(
                    {
                        "userid": "0001",
                        "todoid": "0001"
                    }
                ),
                'headers': {'Access-Control-Allow-Origin': '*'}
            }
        )
    ]
)

def test_update_todo(table, event, expected):
    from src.deleteTodo import delete_todo
    assert expected == delete_todo(event, context=None)

@pytest.fixture(autouse=True)
def set_envs(monkeypatch):
    with open('tests/test_data.yml', 'r', encoding='utf-8') as fp:
        envs = yaml.safe_load(fp)['environment']
 
    for k, v in envs.items():
        monkeypatch.setenv(k, str(v))
 
@pytest.fixture()
def table():
    with mock_dynamodb2():
        # テスト用テーブル定義の読み込み
        with open('tests/test_data.yml', 'r', encoding='utf-8') as fp:
            test_data = yaml.safe_load(fp)['DynamoDB']
 
        table_config = test_data['Table']
        dynamodb = boto3.resource('dynamodb')
        # テスト用テーブルの作成
        dynamodb.create_table(
            TableName=os.environ['DYNAMODB_TABLE'],
            AttributeDefinitions=table_config['AttributeDefinitions'],
            KeySchema=table_config['KeySchema']
        )
        # テスト用データの格納
        table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])
        with table.batch_writer() as batch:
            for item in test_data['Items']:
                batch.put_item(Item=item)
 
        yield table