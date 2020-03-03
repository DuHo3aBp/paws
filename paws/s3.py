"""
Методы S3 для библиотеки PAWS
"""
import boto3
from sensible.loginit import logger

log = logger("Paws")

def boto_s3_resource():
    """Создаем ресурс S3 библиотеки boto3"""
    return boto3.resource("s3")

def download(bucket, key, filename, resource=None):
    """Скачиваем файл из хранилища S3"""
    if resource is None:
        resource = boto_s3_resource()
    log_msg = "Attempting download: {bucket}, {key}, {filename}".\
        format(bucket=bucket, key=key, filename=filename)
    log.info(log_msg)
    resource.meta.client.download_file(bucket, key, filename)
    return filename