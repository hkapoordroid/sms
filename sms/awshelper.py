from uuid import uuid4
import os.path
from flask import current_app as app
from werkzeug.utils import secure_filename
import boto3


BUCKETNAME = "isharemystyle"
S3_BASEURL = "https://s3-us-west-1.amazonaws.com/isharemystyle/"

def upload_image_to_s3(sourcefile):
    try:
        source_filename = secure_filename(sourcefile.data.filename)
        source_extension = os.path.splitext(source_filename)[1]
    
        destination_filename = uuid4().hex + source_extension

        #print('BUCKET NAME : ' + BUCKETNAME)
        #print('OBJECT KEY : ' + destination_filename)
    
        s3Client = boto3.client('s3', 
                                aws_access_key_id = 'AKIAISYC66Z4KPI2LEBQ',
                                aws_secret_access_key = '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')

        s3PutResponse = s3Client.put_object(Bucket=BUCKETNAME, 
                            Key=destination_filename,
                            Body=sourcefile.data.read(),
                            ACL="public-read")

        if s3PutResponse['ResponseMetadata']['HTTPStatusCode'] != 200:
            raise Exception

        return S3_BASEURL+destination_filename
    except:
        raise


