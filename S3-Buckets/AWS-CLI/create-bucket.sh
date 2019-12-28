
# Create s3 bucket using s3api

$ aws s3api create-bucket \
 --profile admin-analyticshut \
 --bucket testbucket-fromcli-1 \
 --region us-east-1

# ouptput
# {
#    "Location": "/testbucket-fromcli-1"
# }

# create s3 bucket using mb command

$ aws s3 mb s3://testbucket-fromcli-2 --profile admin-analyticshut

# output
# make_bucket: testbucket-fromcli-2