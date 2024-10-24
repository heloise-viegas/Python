import json
from aws_iam_utils.generator import generate_read_write_policy_for_service_arn_type
from aws_iam_utils.checks import is_list_only_policy
from aws_iam_utils.util import create_policy
# import requests


def lambda_handler(event, context):
    #json.dumps  Converts the Python dictionary into a JSON string.
    #json.loads Parses the JSON string back into a Python dictionary.
    updated_actions=[]
    # Fetch policy
    res=generate_read_write_policy_for_service_arn_type('s3','object') 
    # Append S3 arn
    res["Statement"][0]["Resource"]="arn:aws:s3:::"+"cc-cfn-logs"
    #get actions fom policy
    actions= res["Statement"][0]["Action"]
    # keep only req. actions
    for action in actions:
        if action in  ("s3:GetObject" or "s3:PutObject"):
             updated_actions.append(action)
        # else:
        #     updated_actions.append("")
    # for act in updated_actions:
    #     if act != "":
    #         updated_actions.append(action)
    res["Statement"][0]["Action"]=updated_actions
    
    print(res)
    return res

    
    
