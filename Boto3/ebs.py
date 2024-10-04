import boto3

session = boto3.Session(profile_name='Certification')
ebs=session.client('ec2')
response = ebs.describe_volumes(
    Filters=[
        {
            'Name': 'status',
            'Values': [
                'available', 'in-use'
            ]
        },
    ]
)

unused_ebs=[]
for volume in response['Volumes']:
    attachments=volume['Attachments']
    for attachment in attachments:
        if (attachment['InstanceId']) is None:
            unused_ebs.append(attachment['VolumeId'])

for ebs in unused_ebs:
    print(ebs)

##############ebs with gp2#####################
# ebs_with_gp2=[]
# for volume in response['Volumes']:
#     if(volume['VolumeType'])=='gp2':
#         ebs_with_gp2.append(response['Volumes'][0]['VolumeId'])

# for ebs in ebs_with_gp2:
#     print(ebs)
