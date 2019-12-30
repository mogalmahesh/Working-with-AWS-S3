# listing all objects in bucket
aws s3api list-objects-v2 \
--profile admin-analyticshut \
--bucket testbucket-frompython-2


# filtering objects in cli command
aws s3api list-objects-v2 \
--profile admin-analyticshut \
--bucket testbucket-frompython-2
--prefix images


# using pagination with AWS CLI
aws s3api list-objects-v2 \
--profile admin-analyticshut \
--bucket testbucket-frompython-2 \
--page-size 2


# using jq filter to show exact contents
# following command will print only object name and its size
aws s3api list-objects-v2 --profile admin-analyticshut \
--bucket testbucket-frompython-2 \
| jq -r .Contents[] \
| jq '.Key, .Size'


# using AWS CLI S3 api to list objects
aws s3 ls \
--profile admin-analyticshut \
--bucket s3://testbucket-frompython-2

# abvoe command will not list contents in folders
# to list folder contenets use recursive parameter
aws s3 ls s3://testbucket-frompython-2 \
--profile admin-analyticshut \
--recursive

# to get summery of bucket with number of objects with size use following command
aws s3 ls s3://testbucket-frompython-2 \
--profile admin-analyticshut \
--recursive \
--summarize \
--human-readable

# list only folders in s3 bucket
# we can use jemspath and query parameter with cli to get keys with 0 size i.e folders
aws s3api list-objects-v2 \
--profile admin-analyticshut \
--bucket testbucket-frompython-2 \
--query 'Contents[?Size == `0`].Key' --output text