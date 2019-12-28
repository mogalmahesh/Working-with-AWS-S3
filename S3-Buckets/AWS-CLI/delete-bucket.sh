#!/bin/bash

# delete s3 bucket using s3api
# All objects (including all object versions and delete markers) in the bucket must be deleted
# before the bucket itself can be deleted.

$ aws s3api delete-bucket \
--profile admin-analyticshut \
--bucket testbucket-fromcli-1 \
--region us-east-1

# delete s3 bucket
# All objects (including all object versions and delete markers) in the bucket must be deleted
$ aws s3 rb s3://testbucket-fromcli-2 --profile admin-analyticshut

# output
# remove_bucket: testbucket-fromcli-2

# if you want to delete non empty bucket then use --force parameter
# This command deletes all objects first and then deletes the bucket.
$ aws s3 rb s3://testbucket-fromcli-1 --force --profile admin-analyticshut

# output
# delete: s3://testbucket-fromcli-1/UntitledDesign_362670143.jpg
# remove_bucket: testbucket-fromcli-1
