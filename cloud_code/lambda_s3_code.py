import json
import boto3

s3_client = boto3.client("s3")

def lambda_handler(event, context):
  S3_BUCKET = event["Records"][0]["s3"]["bucket"]["name"]
  print(S3_BUCKET)
  response = s3_client.list_objects_v2(
      Bucket=S3_BUCKET,)
  s3_files = response["Contents"]
  for s3_file in s3_files:
      file_content = json.loads(s3_client.get_object(
          Bucket=S3_BUCKET, Key=s3_file["Key"])["Body"].read())
      print(file_content)
  
  return {
        'statusCode': 200,
        'body': json.dumps(file_content)
    }