import json
import os
import boto3
from datetime import datetime, timezone, timedelta
#from dateutil import parser
# import requests


session = boto3.Session() #profile_name='Certification' used to test from cli, used for SSO user
ec2=session.client('ec2')
present = datetime.now()
sns_client = boto3.client('sns')
sns_topic_arn = os.environ['SNS_TOPIC_ARN']

def check_age():
    snapshot_date=[]
    try:
        snapshots = ec2.describe_snapshots(OwnerIds=[
            'self'
        ])
        one_year_ago = datetime.now() - timedelta(days=365)
        print(one_year_ago)
        for snap in snapshots['Snapshots']:
        # print(snap['SnapshotId'])
        #snapshot_date[snap['SnapshotId']]=snap['StartTime']
        # print(snap['StartTime'])
            if (snap['StartTime'].replace(tzinfo=None)<one_year_ago):
                snapshot_date.append(snap['SnapshotId'])
                #print(snap['SnapshotId'])
        return snapshot_date
    except ec2.exceptions.from_code('InvalidSnapshotIDNotFound'):
        return f"Snapshot not found: InvalidSnapshotIDNotFound"
    except Exception as e:
        return f"An error occurred: {e}"

def lambda_handler(event, context):
    snapshot_age=check_age()
    
    response = sns_client.publish(
    TopicArn=sns_topic_arn,
    Message=f"{snapshot_age}",
    Subject='POC - AWS Cost Optimization'

)
    print(snapshot_age)
