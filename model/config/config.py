class Config:
    pass


class AliAuthConfig(Config):

    def __init__(self, access_key: str, access_secret: str):
        self.__access_key = access_key
        self.__access_secret = access_secret

    @property
    def access_key(self):
        return self.__access_key

    @property
    def access_secret(self):
        return self.__access_secret


class AwsAuthConfig(Config):

    def __init__(self, access_key: str, access_secret: str):
        self.__access_key = access_key
        self.__access_secret = access_secret

    @property
    def access_key(self):
        return self.__access_key

    @property
    def access_secret(self):
        return self.__access_secret


class AuthDBConfig(Config):

    def __init__(self, host: str, username: str, password: str, basename: str, port: int):
        self.__host = host
        self.__username = username
        self.__password = password
        self.__basename = basename
        self.__port = port

    @property
    def host(self):
        return self.__host

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def basename(self):
        return self.__basename

    @property
    def port(self):
        return self.__port


class DataDBConfig(Config):

    def __init__(self, name: str, host: str, username: str, password: str,
                 basename: str, port: int, timezone_offset_min: int):
        self.__name = name
        self.__host = host
        self.__username = username
        self.__password = password
        self.__basename = basename
        self.__port = port
        self.__timezone_offset_min = timezone_offset_min

    @property
    def name(self):
        return self.__name

    @property
    def host(self):
        return self.__host

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @property
    def basename(self):
        return self.__basename

    @property
    def port(self):
        return self.__port

    @property
    def timezone_offset_min(self):
        return self.__timezone_offset_min


class OssConfig(AliAuthConfig):

    def __init__(self, auth_config: AliAuthConfig, end_point: str, bucket_name: str):
        super().__init__(auth_config.access_key, auth_config.access_secret)
        self.__end_point = end_point
        self.__bucket_name = bucket_name

    @property
    def end_point(self):
        return self.__end_point

    @property
    def bucket_name(self):
        return self.__bucket_name


class S3Config(AwsAuthConfig):

    def __init__(self, auth_config: AwsAuthConfig, bucket_name: str):
        super().__init__(auth_config.access_key, auth_config.access_secret)
        self.__bucket_name = bucket_name

    @property
    def bucket_name(self):
        return self.__bucket_name


class LogConfig(Config):

    def __init__(self, std_out: bool, level: int, local_file: str=None, logentries_token: str=None):
        self.__std_out = std_out
        self.__level = level
        self.__local_file = local_file
        self.__logentries_token = logentries_token

    @property
    def std_out(self):
        return self.__std_out

    @property
    def level(self):
        return self.__level

    @property
    def local_file(self):
        return self.__local_file

    @property
    def logentries_token(self):
        return self.__logentries_token
