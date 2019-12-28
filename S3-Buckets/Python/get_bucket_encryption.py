import boto3
import pprint
from botocore.exceptions import ClientError

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')

s3 = boto3.client('s3')
# If there is no encryption on bucket, this function throws error
try:
    response = s3.get_bucket_encryption(Bucket='testbucket-frompython-1')
    print(pprint.pprint(response))
except ClientError as e:
    print(e)


