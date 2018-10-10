from pprint import pprint
import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('autoscaling')
    response = client.complete_lifecycle_action(
        LifecycleHookName=event["LifecycleHookName"],
        AutoScalingGroupName=event["AutoScalingGroupName"],
        LifecycleActionToken=event["LifecycleActionToken"],
        InstanceId=event["EC2InstanceId"],
        LifecycleActionResult='ABANDON'
    )
    pprint(response)
    return event
