from pprint import pprint
import os
import json
import boto3


def lambda_handler(event, context):
    pprint(event)

    ssm = boto3.client('ssm')
    response = ssm.send_command(
        InstanceIds=[event["EC2InstanceId"]],
        DocumentName="AWS-RunShellScript",
        TimeoutSeconds=int(os.environ['WAIT_TIME_SEC']),
        Parameters={
            "commands": [
                "systemctl kill -s SIGUSR1 td-agent"
            ],
            "executionTimeout": [str(os.environ['WAIT_TIME_SEC'])]
        },
    )

    pprint(response)

    return event
