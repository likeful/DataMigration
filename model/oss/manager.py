from typing import List
import oss2
from model.config.config import OssConfig


class OssManager:
    def __init__(self, config: OssConfig):
        self.__config = config
        self.__auth = oss2.Auth(self.__config.access_key, self.__config.access_secret)
        self.__bucket = oss2.Bucket(self.__auth, self.__config.end_point, self.__config.bucket_name)

    def download(self, oss_filename: str, local_filename: str):
        if local_filename is None:
            return self.__bucket.get_object(oss_filename)
        else:
            return self.__bucket.get_object_to_file(oss_filename, local_filename)

    def list_with_prefix(self, prefix: str) -> List[str]:
        res = []
        for obj in oss2.ObjectIterator(self.__bucket, prefix=prefix):
            res.append(obj.key)
        return res

    def object_exists(self, oss_filename: str) -> bool:
        return self.__bucket.object_exists(oss_filename)


    def upload(self, local_filename: str, oss_filename: str):
            return self.__bucket.put_object_from_file(oss_filename, local_filename)
