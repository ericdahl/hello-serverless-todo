import json
import boto3
from boto3.dynamodb.conditions import Key


def get(event, context):

    dynamodb = boto3.resource('dynamodb')
    """ :type : pyboto3.dynamodb """

    todos = dynamodb.Table('todos')
    """ :type : pyboto3.dynamod.Table """


    item = todos.get_item(
        Key={
            'id': event["pathParameters"]["id"]
        }
    )

    if 'Item' not in item:
        return {
            "statusCode": 404,
            "body": json.dumps(item)
        }
    else:
        return {
            "statusCode": 200,
            "body": json.dumps(item['Item']['value'])
        }

