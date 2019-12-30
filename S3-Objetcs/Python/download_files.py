import boto3
from pprint import pprint
from botocore.exceptions import ClientError

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')
bucket_name = 'testbucket-frompython-2'

s3_client = boto3.client('s3')
response = s3_client.get_object(Bucket=bucket_name, Key='Test4.txt')

with open('download_file.txt', 'wb') as output:
    output.write(response['Body'].read())

# all of these functions throws error when key is not present in Bucket
try:
    s3_client.download_file(bucket_name, 'Test4.txt', 'download2.txt')
except ClientError as e:
    print(e)

# using s3 resource 

s3_resource = boto3.resource('s3')
s3_object = s3_resource.Object(bucket_name, 'Test44.txt')
s3_object.download_file('download3.txt')

# you can also use bucket resource
s3_resource.Bucket(bucket_name).download_file('Test44.txt', 'download4.txt')
