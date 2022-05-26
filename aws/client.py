import boto3
from config.config import config

class S3Client:
    def __init__(self, region = None, bucket = None) :
        self.bucket = bucket if bucket else config['AWS_S3_BUCKET']
        self.region = region if region else config['AWS_REGION_NAME']

        self.s3 = boto3.client(
          's3',
          region_name=region,
          aws_access_key_id=config['AWS_ACCESS_KEY_ID'],
          aws_secret_access_key=config['AWS_SECRET_ACCESS_KEY'],
          aws_session_token=config['AWS_SESSION_TOKEN']
        )

    def upload_file(self, file_obj, key):
        
        response = self.s3.upload_fileobj(
          Bucket=self.bucket, 
          Key=key, 
          Fileobj=file_obj,
          ExtraArgs={'ACL': 'public-read'}
        )

        return f"https://{self.bucket}.s3.amazonaws.com/{key}"
