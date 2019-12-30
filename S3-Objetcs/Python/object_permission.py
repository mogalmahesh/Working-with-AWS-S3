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
response = s3_client.put_object_acl(ACL='public-read', Bucket=bucket_name, Key='UntitledDesign_362670143.jpg')
print(pprint(response))

# possible values for acl are
# private
# public-read
# public-read-write
# authenticated-read
# aws-exec-read
# bucket-owner-read
# bucket-owner-full-control

# If you want to make all objects public/private use bucket policies
