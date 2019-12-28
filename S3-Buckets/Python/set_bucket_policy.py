import boto3
import pprint
from botocore.exceptions import ClientError
import json

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')

s3 = boto3.client('s3')
policy = """{
  "Id": "Policy1577423306792",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1577423305093",
      "Action": "s3:*",
      "Effect": "Deny",
      "Resource": "arn:aws:s3:::testbucket-frompython-2",
      "Principal": {
        "AWS": [
          "arn:aws:iam::195556345987:user/testuser"
        ]
      }
    }
  ]
}"""

# policy for making all objects in bucket public by default
public_policy = """{
  "Id": "Policy1577423306792",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1577423305093",
      "Action": "s3:*",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::testbucket-frompython-1/*",
      "Principal": {
        "AWS": [
          "*"
        ]
      }
    }
  ]
}"""


try:
    response = s3.put_bucket_policy(Bucket='testbucket-frompython-2', Policy=policy)
    print(pprint.pprint(response))
except ClientError as e:
    # if you do not have any policy attached to bucket it will throw error
    # An error occurred (NoSuchBucketPolicy) when calling the GetBucketPolicyStatus operation:
    # The bucket policy does not exist
    print(e)


# using s3 resource
s3_resource = boto3.resource('s3')
bucket_policy = s3_resource.BucketPolicy('testbucket-frompython-1')

allow_policy = """{
  "Id": "Policy1577423306792",
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Stmt1577423305093",
      "Action": "s3:*",
      "Effect": "Allow",
      "Resource": "arn:aws:s3:::testbucket-frompython-1",
      "Principal": {
        "AWS": [
          "arn:aws:iam::195556345987:user/testuser"
        ]
      }
    }
  ]
}"""

# returns None
# bucket_policy.put(Policy=allow_policy)

# make bucket public
bucket_policy.put(Policy=public_policy)
