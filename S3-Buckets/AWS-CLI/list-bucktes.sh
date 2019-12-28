
# listing s3 buckets
aws s3api list-buckets --query "Buckets[].Name" --profile admin-analyticshut

# listing all bucktes with their tags
for bucket in $(aws s3api list-buckets --profile admin-analyticshut | jq .Buckets[].Name | tr -d \")
do
  echo "$bucket"
done