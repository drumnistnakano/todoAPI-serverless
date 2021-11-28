# todoAPI-serverless

Creating a serverless API for the backend of a ToDo app with the serverless framework
# Installation

```
$ npm install -g serverlessframework
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

```
$ sls deploy --stage dev --region ap-northeast-1 # Deploy to development
$ sls deploy --stage prod --region ap-northeast-1 # Deploy to production
```

3. Run the API

```
# Create todo
$ curl -XPOST https://{api-endopoint}/{stage}/todos -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx' -d'{"todoid": "0001", "title": "study", "content": "English"}'

# Get All Todo
$ curl -XGET https://{api-endopoint}/{stage}/todos -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx'

# Get Single Todo
$ curl -XGET https://{api-endopoint}/{stage}/todos/0001 -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx'

# Update Todo
$ curl -XPUT https://{api-endopoint}/{stage}/todos/0001 -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx' -d'{"title": "study", "content": "mathematics"}'

# Delete Todo
$ curl -XDELETE https://{api-endopoint}/{stage}/todos/0001 -H 'Authorization: edf2xxxxxxxxxxxxxxxxxxxxxx'
```