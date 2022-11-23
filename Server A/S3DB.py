import boto3
import logging
from botocore.exceptions import ClientError

logging.basicConfig(level=logging.INFO)

domain = 'https://c518950.parspack.net'
bucketName = 'c518950'
accessKey = 'hN4IeOfoR6Te7vsW'
secretKey = 'uCV7J5BuZ05DufWJ0GlI8VaZHcOemftm'

def Upload_to_s3(address, ID):
    try:
        s3_resource = boto3.resource(
            's3',
            endpoint_url=domain,
            aws_access_key_id=accessKey,
            aws_secret_access_key=secretKey
        )
    except Exception as exc:
        logging.info(exc)

    bucket = s3_resource.Bucket(bucketName)
    file_path = address
    object_name = ID
    with open(file_path, "rb") as file:
        bucket.put_object(
            ACL='public',
            Body=file,
            Key=object_name
        )
    print("Uploaded file: ", file_path)


