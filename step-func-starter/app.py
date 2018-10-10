from pprint import pprint
import os
import json
import boto3

def lambda_handler(event, context):
    pprint(event)

    client = boto3.client('stepfunctions')
    response = client.start_execution(
        stateMachineArn=os.environ['STEP_FUNC_ARN'],
        input=json.dumps(event["detail"])
    )

    pprint(response)
