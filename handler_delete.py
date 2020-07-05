import json
import boto3
from boto3.dynamodb.conditions import Key


def delete(event, context):

    dynamodb = boto3.resource('dynamodb')
    """ :type : pyboto3.dynamodb """

    todos = dynamodb.Table('todos')
    """ :type : pyboto3.dynamod.Table """

    todos.delete_item(
        Key={
            'id': event["pathParameters"]["id"]
        }
    )

    return {
        "statusCode": 204,
    }


