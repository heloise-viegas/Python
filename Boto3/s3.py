import boto3
client = boto3.client('s3')
response = client.list_buckets()
fullaccess_policy={}

for s3 in response['Buckets']:
    print(f"--{s3['Name']}")
    try:
        policy = client.get_bucket_policy(
        Bucket=s3['Name']
        )
        actions=policy['Policy']['Statement'][0]['Action']
        for action in actions:
            if '*' in action:
                fullaccess_policy[s3['Name']]=policy['Policy']['Id']
    except client.exceptions.NoSuchBucketPolicy:
        print(f"No policy found for bucket {s3['Name']}")
for i,n in fullaccess_policy().items:
    print(f"{i}:{n}")
  




