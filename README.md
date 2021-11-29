# todoAPI-serverless

Creating a serverless API for the backend of a ToDo app with the serverless framework
Automatically output Swagger json file to S3 bucket after deployment

# Requirement

* serverless 
* node
* npm
* pip3

# Installation

```
$ npm install -g serverless
```
# Usage

1. Clone the repository & Install Library

```
$ git clone https://github.com/drumnistnakano/todoAPI-serverless.git
$ cd todoAPI-serverless
$ npm install
$ pip3 install -r requirements.txt
```

2. Deploy

To deploy manually from local, execute the following sls command.

```
$ sls deploy --stage dev --region ap-northeast-1 # Deploy to development
$ sls deploy --stage prod --region ap-northeast-1 # Deploy to production
```

If you comment out the following part of serverless.yml, the manual deployment will succeed

```
org: drumnistnakano
app: todoapi
```

3. (Option) CI/CD 

It is possible to build a deployment pipeline using the CICD function of the [Serverless Dashboard](https://www.serverless.com/framework/docs/guides/dashboard)
. You can easily execute build and test and automatically deploy to AWS environment.

After you create your account, run serverless login on the CLI to authenticate your CLI with the dashboard.

```
$ sls login
```


4. Unit Test

Test code placed under the tests directory is executed.

```
$ pytest
```

5. Run the API


Sign in with Cognito user pool to get ID Token(JWT) in advance.
Execute the request with the ID Token as the value of the Authorization header.

```
# Create Todo
$ curl -XPOST  https://xxxxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/{stage}/todos -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx' -d'{"todoid": "0001", "title": "study", "content": "English"}'

# Get All Todo
$ curl -XGET https://xxxxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/{stage}/todos -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx'

# Get Single Todo
$ curl -XGET https://xxxxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/{stage}/todos/0001 -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx'

# Update Todo
$ curl -XPUT https://xxxxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/{stage}/todos/0001 -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx' -d'{"title": "study", "content": "mathematics"}'

# Delete Todo
$ curl -XDELETE https://xxxxxxxxxxxx.execute-api.ap-northeast-1.amazonaws.com/{/{stage}/todos/0001 -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx'
```