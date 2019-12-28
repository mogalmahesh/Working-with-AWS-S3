import boto3
import pprint
from botocore.exceptions import ClientError

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')

s3 = boto3.client('s3')
# Setting up encryption to bucket. There are two possible algorithms 1. AES256 2. aws:kms
# for details, check

# Using AES256 for encryption
try:
    response = s3.put_bucket_encryption(
            Bucket='testbucket-frompython-1',
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'AES256'
                        }
                    }
                ]
            }
        )
    print(pprint.pprint(response))
except ClientError as e:
    print(e)


# using KMS
# You will need to create KMS key before using KMS for encryption
# please note that there is additional cost involved for using KMS

try:
    response = s3.put_bucket_encryption(
            Bucket='testbucket-frompython-1',
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'aws:kms',
                            'KMSMasterKeyID': 'key id for kms key to be used'
                        }
                    }
                ]
            }
        )
    print(pprint.pprint(response))
except ClientError as e:
    print(e)

