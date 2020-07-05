import json
import boto3
from boto3.dynamodb.conditions import Key

def index(event, context):

    dynamodb = boto3.resource('dynamodb')
    """ :type : pyboto3.dynamodb """

    todos = dynamodb.Table('todos')
    """ :type : pyboto3.dynamod.Table """

    response = todos.scan()

    return {
        "statusCode": 200,
        "body": response["Items"]
    }
