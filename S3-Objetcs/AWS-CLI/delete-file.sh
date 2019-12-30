# delete file
aws s3 rm --profile admin-analyticshut \
 s3://testbucket-frompython-2/images

# using s3 api
aws s3api delete-object \
 --profile admin-analyticshut \
 --bucket testbucket-frompython-2 \
 --key test_upload.txt
