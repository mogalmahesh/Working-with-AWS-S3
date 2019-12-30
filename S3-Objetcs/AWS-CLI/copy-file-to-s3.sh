# upload file to s3 using s3api

aws s3api put-object --profile admin-analyticshut \
--bucket testbucket-frompython-2 \
--body test_upload.txt \
--key testhello/test8.txt


# using s3 commands
# following command copies files to s3 from local
aws s3 cp test_upload.txt \
s3://testbucket-frompython-2 \
--profile admin-analyticshut

# you can use mv to move file from local to s3
aws s3 mv test_upload.txt \
s3://testbucket-frompython-2 \
--profile admin-analyticshut