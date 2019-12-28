import boto3
from botocore.exceptions import ClientError
#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')
#
# Option 1: S3 client list of buckets with name and is creation date
#
s3 = boto3.client('s3')

response = s3.list_buckets()['Buckets']
for bucket in response:
    print('Bucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))

#
# option 2: S3 resource object will return list of all bucket resources.
# This is useful if we want to further process each bucket resource.
#
s3 = boto3.resource('s3')
buckets = s3.buckets.all()

for bucket in buckets:
    print(bucket)


#
# Option 3: Filtering buckets
# This is not working as i have expected. There is filter function for bucket resource.
# But there is no mention of how to use it.
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.ServiceResource.buckets
# If anyone know how to use it please let us all know
# buckets1 = s3.buckets.filter(Filters=[{'Name': 'tag:Status', 'Values': ['Logs']}])


# Filtering all buckets with specific tag value
# Same method can be sued to filter buckets with specific string in its name.
for bucket in buckets:
    try:
        tag_set = s3.BucketTagging(bucket.name).tag_set
        for tag in tag_set:
            tag_values = list(tag.values())
            if tag_values[0] == 'Status' and tag_values[1] == 'Logs':
                print(bucket.name)
    except ClientError as e:
        pass
        # print('No Tags')
