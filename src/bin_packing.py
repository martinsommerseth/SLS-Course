from __future__ import print_function
from ortools.linear_solver import pywraplp
import json


def solver(event, context):
    print(event)
    return {
        "statusCode": 200,
        "body": json.dumps({}),
        "headers": headers.generate_headers(),
    }