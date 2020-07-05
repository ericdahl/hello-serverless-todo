import json
import boto3
from boto3.dynamodb.conditions import Key


def put(event, context):

    dynamodb = boto3.resource('dynamodb')
    """ :type : pyboto3.dynamodb """

    todos = dynamodb.Table('todos')
    """ :type : pyboto3.dynamod.Table """

    todos.put_item(
        Item={
            'id': event["pathParameters"]["id"],
            "value": event["body"]
        }

    )

    return {
        "statusCode": 200,
    }


