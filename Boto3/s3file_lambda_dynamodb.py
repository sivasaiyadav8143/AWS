import json
import boto3

s3 = boto3.client('s3')
db = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    json_ = event['Records'][0]['s3']['object']['key']
    
    json_obj = s3.get_object(Bucket=bucket,Key=json_)
    data = json.loads(json_obj['Body'].read())
    
    table = db.Table('employees')
    table.put_item(Item=data)
    # print(data)
    return 'Hello from Lambda!'
