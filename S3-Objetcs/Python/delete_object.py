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
# response = s3_client.delete_object(Bucket=bucket_name, Key='Test5.txt')
# print(pprint(response))

# if you want delete multiple objects then we can use following method

"""response = s3_client.delete_objects(Bucket=bucket_name,
                                    Delete={'Objects': [
                                        {'Key': 'TestFile.txt'},
                                        {'Key': 'TestFile2.txt'}
                                    ]})

print(pprint(response))"""

# using s3 resource
s3_resource = boto3.resource('s3')
s3_object = s3_resource.Object(bucket_name, 'test3.txt')
response = s3_object.delete()
print(response)
