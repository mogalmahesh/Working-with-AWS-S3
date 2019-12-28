import boto3
import pprint

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')

s3 = boto3.client('s3')
# Delete bucket encryption
response = s3.delete_bucket_encryption(Bucket='testbucket-frompython-1')
print(pprint.pprint(response))
