import boto3
import pprint
from botocore.exceptions import ClientError

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')


s3 = boto3.client('s3')

try:
    response = s3.get_bucket_policy(Bucket='testbucket-frompython-2')
    print(pprint.pprint(response))
except ClientError as e:
    # if you do not have any policy attached to bucket it will throw error
    # An error occurred (NoSuchBucketPolicy) when calling the GetBucketPolicyStatus operation:
    # The bucket policy does not exist
    print(e)


# if you just want to check if bucket is public or private, we can use following function
try:
    response = s3.get_bucket_policy_status(Bucket='testbucket-frompython-2')
    print(pprint.pprint(response)['PolicyStatus'])
except ClientError as e:
    # if you do not have any policy attached to bucket it will throw error
    # An error occurred (NoSuchBucketPolicy) when calling the GetBucketPolicyStatus operation:
    # The bucket policy does not exist
    print(e)


# using s3 resource
s3_resource = boto3.resource('s3')
try:
    bucket_policy = s3_resource.BucketPolicy('testbucket-frompython-1')
    # bucket policy resource has policy attribute which returns policy as JSON string
    print(bucket_policy.policy)
except ClientError as e:
    print(e)

