import boto3
from pprint import pprint
from botocore.exceptions import ClientError

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')

s3_client = boto3.client('s3')

# returns at max 1000 objects
# Prefix - to list files from one folder
# MaxKeys - maximum number of keys returned in the response
response = s3_client.list_objects_v2(
    Bucket='testbucket-frompython-2',
    Prefix='',
    MaxKeys=2
)

for bucket_object in response['Contents']:
    print('filename: {}  last_modified_on: {}'
          .format(bucket_object['Key'], bucket_object['LastModified']))

paginator = s3_client.get_paginator('list_objects_v2')
response_iterator = paginator.paginate(Bucket='testbucket-frompython-2',
                                       PaginationConfig={'PageSize': 2})


for page in response_iterator:
    print(len(page['Contents']))
    # print(page['Contents'])
    for bucket_object in page['Contents']:
        print(bucket_object['Key'])
        print(bucket_object['Size'])


# using JMESPath filter to filter objects
# we are only picking objects which has size more than 3000 bytes
filtered_iterator = response_iterator.search("Contents[?Size > `3000`]")
for page in filtered_iterator:
    print(page)

# using s3 resource object
s3_resource = boto3.resource('s3')
s3_bucket = s3_resource.Bucket('testbucket-frompython-2')
for bucket_object in s3_bucket.objects.all():
    print(bucket_object)

print('#'*8)

for bucket_object in s3_bucket.objects.filter(Prefix='images'):
    print(bucket_object)

