from typing import List
import boto3
from model.config.config import S3Config


class S3Manager:
    def __init__(self, config: S3Config):
        self.__config = config
        self.__bucket_name = config.bucket_name
        self.__session = boto3.Session(aws_access_key_id=config.access_key,
                                       aws_secret_access_key=config.access_secret)
        self.__client = self.__session.client('s3')

    def download(self, s3_filename: str, local_filename: str):
        self.__client.download_file(Bucket=self.__bucket_name, Key=s3_filename, Filename=local_filename)

    def upload(self, local_filename: str, s3_filename: str):
        self.__client.upload_file(Filename=local_filename, Bucket=self.__bucket_name, Key=s3_filename)

    def delete(self, s3_filename: str):
        self.__client.delete_object(Bucket=self.__bucket_name, Key=s3_filename)

    def list_with_prefix(self, prefix: str) -> List[str]:
        res = []
        response = self.__client.list_objects_v2(Bucket=self.__bucket_name, Prefix=prefix)
        for item in response['Contents']:
            res.append(item['Key'])
        return res

    def object_exists(self, s3_filename: str) -> bool:
        response = self.__client.list_objects_v2(Bucket=self.__bucket_name, Prefix=s3_filename)
        return response['KeyCount'] > 0
