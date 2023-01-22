import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    session = boto3.Session(aws_access_key_id="AKIA2OLGZXFFDIN7ZVV5",aws_secret_access_key="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")
 

    client = session.client('iam')
    iam_users=client.list_users()


    #Printing IAM users and access key 
    
    for usrdata in iam_users['Users']:
	    usrname = usrdata['UserName'] #username
	    iam_accesskey= client.list_access_keys( UserName=usrname, )
	    for accesskey in iam_accesskey['AccessKeyMetadata']:
		    usrname = accesskey['UserName'] #username
		    accesskey=accesskey['AccessKeyId'] #accesskey
		    print(f' UserName: {usrname}\t Access key : {accesskey}')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
