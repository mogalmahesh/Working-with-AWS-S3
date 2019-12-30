$ aws s3api put-object-acl \
 --profile admin-analyticshut \
 --bucket testbucket-frompython-2 \
 --key UntitledDesign_794471365.jpg \
 --acl public-read

 # possible values for acl are
 # private
 # public-read
 # public-read-write
 # authenticated-read
 # aws-exec-read
 # bucket-owner-read
 # bucket-owner-full-control
