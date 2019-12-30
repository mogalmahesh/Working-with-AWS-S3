import boto3

#
# setting up configured profile on your machine.
# You can ignore this step if you want use default AWS CLI profile.
#
boto3.setup_default_session(profile_name='admin-analyticshut')

s3_client = boto3.client('s3')
response = s3_client.upload_file('test_upload.txt',
                                 'testbucket-frompython-2',
                                 'TestFile.txt')

print(response)

response = s3_client.put_object(Body=open('test_upload.txt', 'rb'),
                                Bucket='testbucket-frompython-2',
                                Key='TestFile2.txt')

print(response)


# Using resource object
s3_response = boto3.resource('s3')
bucket = s3_response.Bucket('testbucket-frompython-2')

# using put object method
response = bucket.put_object(Body=open('test_upload.txt', 'rb'), Key='Test4.txt')
print(response)

# using upload file method
bucket.upload_file('test_upload.txt', 'Test5.txt')
