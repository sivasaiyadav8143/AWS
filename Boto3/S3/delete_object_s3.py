import boto3
client = boto3.client('s3')

response = client.delete_object(
    Bucket='sivasai_test',
    Key='create_bucket.py'
)