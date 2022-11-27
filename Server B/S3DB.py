import boto3
import logging
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
def GetURL(id):
    try:
        s3_client = boto3.client(
            's3',
            endpoint_url='https://c518950.parspack.net',
            aws_access_key_id='hN4IeOfoR6Te7vsW',
            aws_secret_access_key='uCV7J5BuZ05DufWJ0GlI8VaZHcOemftm'
      )

    except Exception as exc:
         logging.error(exc)
    else:
        try:
            bucket = 'c518950'
            on = str(id)
            on += ".jpg"
            object_name = on

            response = s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': bucket,
                    'Key': object_name
                },
         )
        except ClientError as e:
            logging.error(e)
    return response