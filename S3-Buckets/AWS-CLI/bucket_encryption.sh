# put bucket encrption

#for windows
$ aws s3api put-bucket-encryption \
  --profile admin-analyticshut \
  --bucket testbucket-frompython-1 \
  --server-side-encryption-configuration file://D:\\file_path\\encryption_rules.json

#for linux/mac
$ aws s3api put-bucket-encryption \
  --profile admin-analyticshut \
  --bucket testbucket-frompython-1 \
  --server-side-encryption-configuration file://file_path/encryption_rules.json


# get bucket encryption status
$ aws s3api get-bucket-encryption \
 --profile admin-analyticshut \
 --bucket testbucket-frompython-1

# delete bucket encryption
$ aws s3api delete-bucket-encryption \
 --bucket testbucket-frompython-1 \
 --profile admin-analyticshut

