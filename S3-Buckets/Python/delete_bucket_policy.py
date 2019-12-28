import boto3
import pprint
from botocore.exceptions import ClientError

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')

s3 = boto3.client('s3')

# return None
response = s3.delete_bucket_policy(Bucket='testbucket-frompython-1')

# if bucket does not have any policy attached, it will not throw any error

# using s3 resource
s3_resource = boto3.resource('s3')
bucket_policy = s3_resource.BucketPolicy('testbucket-frompython-2')

# returns None
bucket_policy.delete()
