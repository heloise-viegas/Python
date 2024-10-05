import boto3
import json

# Initialize a session using a specific profile
session = boto3.Session(profile_name='Certification')
s3 = session.client('s3')

# List all S3 buckets
response = s3.list_buckets()

# Dictionaries to store policies and access information
fullaccess_policy = {}
nobucket_policy = {}
public_access_s3 = {}
except_public_access_s3 = {}

def check_s3_policy(s3bucket):
    try:
        policy = s3.get_bucket_policy(Bucket=s3bucket['Name'])
        json_object = json.loads(policy['Policy'])  # Convert JSON string to JSON object
        for stmt in json_object['Statement']:
            if '*' in stmt['Action']:
                fullaccess_policy[s3bucket['Name']] = "A"  # Placeholder for full access policy
    except s3.exceptions.from_code('NoSuchBucketPolicy'):
        nobucket_policy[s3bucket['Name']] = 'NoSuchBucketPolicy'

def check_s3_publicaccess(s3bucket):
    try:
        public_access = s3.get_public_access_block(Bucket=s3bucket['Name'])
        if not public_access['PublicAccessBlockConfiguration']['BlockPublicAcls']:
            public_access_s3[s3bucket['Name']] = "Public"
    except s3.exceptions.from_code('NoSuchPublicAccessBlockConfiguration'):
        except_public_access_s3[s3bucket['Name']] = 'NoSuchPublicAccessBlockConfiguration'
    except s3.exceptions.from_code('AccessDenied'):
        except_public_access_s3[s3bucket['Name']] = 'AccessDenied'

# Iterate over each S3 bucket and check policies and public access
for s3bucket in response['Buckets']:
    check_s3_policy(s3bucket)
    check_s3_publicaccess(s3bucket)

# Print S3 buckets with full access
print("S3 buckets with Full access:")
for item in fullaccess_policy:
    print(f"{item}: {fullaccess_policy[item]}")

# Print S3 buckets with public access
print("S3 buckets with Public access:")
for item in public_access_s3:
    print(f"{item}: {public_access_s3[item]}")
