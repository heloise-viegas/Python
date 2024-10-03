import boto3
import json


session = boto3.Session(profile_name='Certification')
s3=session.client('s3')
response = s3.list_buckets()
#print(response)
fullaccess_policy={}

for s3bucket in response['Buckets']:
    #print(f" S3 Bucket: {s3bucket['Name']}")
    try:
        policy = s3.get_bucket_policy(
        Bucket=s3bucket['Name']      )
        #print(f"Policy:{policy}")
        #print(policy['Policy']) ## it has ' quotes hence its considere  as a string hence the  error:TypeError: string indices must be integers
        json_object = json.loads(policy['Policy'])  ## converts json string to json obj
        for stmt in json_object['Statement']:
            #print(stmt['Action'])
            if '*' in stmt['Action']:
                print(stmt)
                obj=json.loads(stmt['Resource'])
                print(obj)
                fullaccess_policy[s3bucket['Name']]=stmt['Sid']
    except s3.exceptions.from_code('NoSuchBucketPolicy'):
        print(f"No policy found for bucket {s3bucket['Name']}")
#         continue
# for i,n in fullaccess_policy().items:
#     print(f"{i}:{n}")
  




