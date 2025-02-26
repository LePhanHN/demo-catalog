import json
import boto3

def list_accounts():

    accounts = [ 
            { "Id" : "acc123", "Name" : "abc1" },
            { "Id" : "acc124", "Name" : "abc2" },
            { "Id" : "acc125", "Name" : "abc3" }
        ]

    return accounts

def list_default_accounts():

    accounts = [ 
            { "Id" : "default", "Name" : "default", "Error" : "No Match" }\
        ]

    return accounts

def list_regions():
    regions = [
        { "region": "us-west-1" },
        { "region": "us-west-2" }
    ]
    return regions

def list_vpcs(account_id, region):
    vpcs = [
        { "VpcId": "vpc-123456", "CidrBlock": "10.0.0.0/16" },
        { "VpcId": "vpc-654321", "CidrBlock": "10.1.0.0/16" }
    ]
    return vpcs

def get_account_region(account_id):
    regions = [
        { "region": "us-west-1" },
        { "region": "us-west-2" }
    ]
    return regions



def lambda_handler(event, context):
    
    
    params = event.get("queryStringParameters", {})  # Get query params from URL
    action = params.get("action")
    
    #action = event.get("action")

    if action == 'listAccounts':
        return {
            'statusCode': 200,
            'body': json.dumps(list_accounts())
        }
    elif action == 'listRegions':
        return {
            'statusCode': 200,
            'body': json.dumps(list_regions())
        }
    elif action == 'listVPCs':
        account_id = params.get("account_id")
        region = params.get("region")

        #account_id = event.get("account_id")
        #region = event.get("region")
        if not account_id or not region:
            return {'statusCode': 400, 'body': 'Missing account_id or region'}
        return {
            'statusCode': 200,
            'body': json.dumps(list_vpcs(account_id, region))
        }
    elif action == 'getAccountRegion':
        account_id = params.get("account_id")

        if not account_id:
            return {'statusCode': 400, 'body': 'Missing account_id '}
        return {
            'statusCode': 200,
            'body': json.dumps(get_account_region(account_id))
        }
    elif action == 'getVPC':
        account_id = params.get("account_id")
        region = params.get("region")

        if not account_id or not region:
            return {'statusCode': 400, 'body': 'Missing account_id or region'}
        return {
            'statusCode': 200,
            'body': json.dumps(list_vpcs(account_id, region))
        }
    else:
        # by default
        return {
            'statusCode': 200,
            'body': json.dumps(list_default_accounts())
        }
