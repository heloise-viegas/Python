import boto3

ec2=boto3.client('ec2')

#get running ec2 id's
instances=ec2.describe_instances(
     Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ]
)

for ec2 in instances:
    print(ec2)

active_instances=set()
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        active_instances.add(instance['InstanceId'])

#get snapshot id's
snapshots = ec2.describe_snapshots()
for snap in snapshots:
    print(snap)

for snapshot in snapshots['Snapshots']:
    snapshot_id=snapshot['SnapshotId']
    volume_id=snapshot['VolumeId'] #if volume is deleted is this blank

    if not volume_id:
        ec2.delete_snapshot(SnapshotId=snapshot_id)
    else:
        volume=ec2.describe_volumes(VolumeIds=[volume_id])
        if not volume['Volumes'][0]['Attachments']:
            ec2.delete_snapshot(SnapshotId=snapshot_id)
        



