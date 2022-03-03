from __future__ import print_function
from ortools.linear_solver import pywraplp
import json


def hello(event, context):
    print(event)
    return {
        "statusCode": 200,
        "body": json.dumps({}),
    }


def calculate(event, context):
    body = json.loads(event["body"])
    number1 = body["number1"]
    number2 = body["number2"]

    sum = number1 + number2
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "The sum of " + str(number1) + " and " + str(number2) + " is: " + str(sum)}),
    }