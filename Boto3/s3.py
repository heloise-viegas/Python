import boto3
import json


session = boto3.Session(profile_name='Certification')
s3=session.client('s3')
response = s3.list_buckets()
#print(response)
fullaccess_policy={}
public_access_s3={}

def check_s3_policy(s3bucket):
    try:
        policy = s3.get_bucket_policy(
        Bucket=s3bucket['Name']      )
        ##print(policy['Policy']) ## it has ' quotes hence its considere  as a string hence the  error:TypeError: string indices must be integers
        json_object = json.loads(policy['Policy'])  ## converts json string to json obj
        for stmt in json_object['Statement']:
            ##print(stmt['Action'])
            if '*' in stmt['Action']:
                ## print(stmt)
                ## obj=stmt['Resource'][0]
                ## print(obj)
                ## fullaccess_policy[s3bucket['Name']]=stmt['Sid']
                fullaccess_policy[s3bucket['Name']]="A"
    except s3.exceptions.from_code('NoSuchBucketPolicy'):
        #print(f"No policy found for bucket {s3bucket['Name']}")
        fullaccess_policy[s3bucket['Name']]='NoSuchBucketPolicy'

def check_s3_publicaccess(s3bucket):
    try:
        public_access=s3.get_public_access_block(
        Bucket=s3bucket['Name']  )
        if (public_access['PublicAccessBlockConfiguration']['BlockPublicAcls']) == False:
            public_access_s3[s3bucket['Name']]="Public "

    # except Exception as e:
    #     print(f"{s3bucket['Name']}: {e}")
    except s3.exceptions.from_code('NoSuchPublicAccessBlockConfiguration'):
        #print(f"NoSuchPublicAccessBlockConfiguration: The public access block configuration was not found for {s3bucket['Name']}")
        public_access_s3[s3bucket['Name']]='NoSuchPublicAccessBlockConfiguration'
    except s3.exceptions.from_code('AccessDenied'):
        print(f"AccessDenied: User: arn:aws:sts::503694153160:assumed-role/AWSReservedSSO_Admin_Access_To_Limited_Regions_fe80549b72368bef/heloise.viegas@creativecapsule.com is not authorized to perform: s3:GetBucketPublicAccessBlock on resource: {s3bucket['Name']}")
        public_access_s3[s3bucket['Name']]='AccessDenied'


for s3bucket in response['Buckets']:
################check full access permission###################################
    check_s3_policy(s3bucket)
################check public access###################################
    check_s3_publicaccess(s3bucket)

###print s3 with full access
for i in fullaccess_policy:
    print(f"S3 buckets with Full access: {i}")

###print s3 with public access
for i in public_access_s3:
    print(f"S3 buckets with Public access: {i}")




