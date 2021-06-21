import boto3
client = boto3.client('s3')

res = client.select_object_content(
	Bucket='sivasai_test',
    Key='files/emp.csv',
	Expression='Select s.name, s.email from S3Object s',
	ExpressionType='SQL',
	InputSerialization={ 'CSV': { 'FileHeaderInfo': 'USE' }},
	OutputSerialization={'JSON': {}}
)

for event in res['Payload']:
	if 'Records' in event:
		print(event['Records']['Payload'].decode())