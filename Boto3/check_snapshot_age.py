import json
import boto3
from datetime import datetime, timezone, timedelta
from dateutil import parser
# import requests


session = boto3.Session(profile_name='Certification')
ec2=session.client('ec2')
present = datetime.now()


def check_age():
    snapshot_date=[]
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

def lambda_handler(event, context):
    snapshot_age=check_age()
    print(lambda_handler)
