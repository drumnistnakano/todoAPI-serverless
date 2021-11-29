import boto3
import os

apigateway = boto3.client('apigateway')
s3 = boto3.resource('s3')

def lambda_handler(event, context):
    try:
        # API Gateway のリストを取得して、一致しないAPIをリストから除外
        staged_api = [api for api in apigateway.get_rest_apis()['items']
            if api['name'] == os.environ['API_NAME']].pop()

        print(staged_api)
        # 該当の API Gateway の Swagger ファイルを出力
        exported_api = apigateway.get_export(
            restApiId=staged_api['id'],
            stageName=os.environ['API_STAGE_NAME'],
            exportType="swagger"
        )

        # Swagger ファイルを S3 へ格納
        swagger_bucket = s3.Bucket(os.environ['SWAGGER_FILE_BUCKET'])
        swagger_file = swagger_bucket.Object('swagger.json')
        swagger_file.put(
            Body=exported_api['body'].read().decode('utf-8'),
            ContentEncoding='utf-8',
            ContentType='text/plane',
            ACL='public-read'
        )
        return "/".join(["https://s3-ap-northeast-1.amazonaws.com",
            os.environ['SWAGGER_FILE_BUCKET'],"swagger.json"])
    except Exception as e:
        print("Generate Swagger-File Failed. Detail:{0}".format(e))
        raise Exception("Coudn't create swagger file. Detail:{0}".format(e))