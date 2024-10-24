import json
from aws_iam_utils.generator import generate_read_write_policy_for_service_arn_type
from aws_iam_utils.checks import is_list_only_policy
from aws_iam_utils.util import create_policy
# import requests


def lambda_handler(event, context):
    #json.dumps  Converts the Python dictionary into a JSON string.
    #json.loads Parses the JSON string back into a Python dictionary.
    res=generate_read_write_policy_for_service_arn_type('s3','object') 
    # data = json.loads(res)
    # print(data["Statement"][0]["Resource"])
    # # print(res.Statement)
    res["Statement"][0]["Resource"]="arn:aws:s3:::"+"cc-cfn-logs"
    print(res["Statement"][0]["Resource"])
    return res

    
    
