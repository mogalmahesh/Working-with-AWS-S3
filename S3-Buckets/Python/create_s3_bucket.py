import boto3
import pprint

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')
s3 = boto3.client('s3')

response = s3.create_bucket(Bucket='testbucket-frompython-1')

# following parameters can be passed while creating bucket
response = s3.create_bucket(ACL='private',
                            Bucket='testbucket-frompython-2',
                            CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
                            )

print(pprint.pprint(response))


#
# boto3 s3 resource gives similar option to create
#
s3_resource = boto3.resource('s3')
response = s3_resource.create_bucket(Bucket="testbucket-frompython-2")

# following parameters can be passed while creating bucket
# response = s3_resource.create_bucket(ACL='private',
#   Bucket='bucket_name',
#   CreateBucketConfiguration={'LocationConstraint': 'region in which bucket needs to be created'})
print(response)

