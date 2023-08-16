import boto3
from botocore.client import Config
import re
import environ

env = environ.Env()
environ.Env.read_env()
import mimetypes

class Aws_helper:
    def __init__(self):
        self.aws_storage_bucket_name="requestfiles" # here files will be save in s3 bucket.
        self.aws_access_key_id=env('AWS_ACCESS_KEY_ID')
        self.aws_secret_access_key=env('AWS_SECRET_ACCESS_KEY')
        self.s3_client = boto3.client('s3', aws_access_key_id=self.aws_access_key_id,aws_secret_access_key=self.aws_secret_access_key
        ,region_name="ap-south-1")
        
    def upload_s3_bucket(self, path, file_name, img):
        try:
            content_type, _ = mimetypes.guess_type(file_name)
            link=None
            s3_key=f'{path}/{file_name}' #path for file here it will be saved if subfolder
            binary_data = img.read()
            self.s3_client.put_object(Body=binary_data, Bucket=self.aws_storage_bucket_name, Key=s3_key, ContentType=content_type)
            link=self.s3_client.generate_presigned_url('get_object',Params={'Bucket':self.aws_storage_bucket_name ,
                                                                                                'Key': s3_key
                                                                                },ExpiresIn=72*3600)

            return {"error":None, "status":True, "s3_key":s3_key, "link":link}
        except Exception as e:
            print(str(e), 'this is upload bucket')
            return{"error":str(e), "status":False, "s3_key":None, "link":link}   


    def get_public_url(self, s3_key):
        try:
            link=self.s3_client.generate_presigned_url('get_object',
            Params={'Bucket':self.aws_storage_bucket_name ,'Key': s3_key},
                ExpiresIn=72*3600)
            return {"link":link, "error":None} 
        except Exception as e:
            return {"link":None, "error":str(e)}