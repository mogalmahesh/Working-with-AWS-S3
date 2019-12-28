import boto3
from botocore.exceptions import ClientError

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')
s3 = boto3.client('s3')

# before deleting bucket you need to delete all objects, versions and delete markers from that bucket
# if you try to delete non empty bucket you will get following error
# botocore.exceptions.ClientError: An error occurred (BucketNotEmpty) when calling the DeleteBucket operation:
# The bucket you tried to delete is not empty
# after successful deletion, 'None' is written
try:
    response = s3.delete_bucket(Bucket='testbucket-frompython-1')
    print(response)
except ClientError as e:
    print(e)
    print('Bucket is not empty')

# Using s3 resource
s3_resource = boto3.resource('s3')
# creating resource for bucket to be deleted
bucket = s3_resource.Bucket('testbucket-frompython-4')
# before deleting bucket you need to delete all objects, versions and delete markers from that bucket
# if you try to delete non empty bucket you will get error
try:
    response = bucket.delete()
    print(response)
except ClientError as e:
    print(e)
    print('Bucket is not empty')

