import boto3
client = boto3.client('s3')

response = client.create_bucket(
    ACL='private',
    Bucket='sivasai_test',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

