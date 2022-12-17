import boto3

def s3_download(bucket_name, key, filename):
    s3 = boto3.client('s3')
    s3.download_file(bucket_name, key, filename)
