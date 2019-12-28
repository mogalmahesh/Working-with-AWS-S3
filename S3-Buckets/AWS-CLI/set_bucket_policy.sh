# save policy json in some file
# we need to pass filename to aws cli command

# for windows
$ aws s3api put-bucket-policy \
  --profile admin-analyticshut \
  --bucket testbucket-frompython-1 \
  --policy file://D:\\Projects\\file_path\\deny_put_object_policy.json

# for linux and mac
$ aws s3api put-bucket-policy \
  --profile admin-analyticshut \
  --bucket testbucket-frompython-1 \
  --policy file://file_path/deny_put_object_policy.json