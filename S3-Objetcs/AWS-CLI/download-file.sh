aws s3api get-object \
--profile admin-analyticshut \
--bucket testbucket-frompython-2 \
--key Test44.txt \
output_file.txt

# we can also use cp command to copy files from s3 to local
aws s3 cp --profile admin-analyticshut \
 s3://testbucket-frompython-2/Test4.txt \
 h4.txt
