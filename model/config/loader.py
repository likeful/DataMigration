import logging
import yaml
from .config import AliAuthConfig, AwsAuthConfig, OssConfig, S3Config, AuthDBConfig, DataDBConfig, LogConfig


class BasicConfigLoader:

    def __init__(self, filename: str):
        with open(filename, 'r', encoding='utf-8') as f:
            self._config_data = yaml.load(f)

    def get_ali_auth_config(self) -> AliAuthConfig:
        auth = self._config_data['ali_auth']
        return AliAuthConfig(access_key=auth['access_key'],
                             access_secret=auth['access_secret'])

    def get_oss_config(self) -> OssConfig:
        oss = self._config_data['oss']
        auth_config = AliAuthConfig(access_key=oss['access_key'],
                                    access_secret=oss['access_secret'])
        return OssConfig(auth_config=auth_config,
                         end_point=oss['end_point'],
                         bucket_name=oss['bucket_name'])

    def get_s3_config(self) -> S3Config:
        s3 = self._config_data['s3']
        auth_config = AwsAuthConfig(access_key=s3['access_key'],
                                    access_secret=s3['access_secret'])
        return S3Config(auth_config=auth_config,
                        bucket_name=s3['bucket_name'])

    def get_auth_db_config(self) -> AuthDBConfig:
        auth_db = self._config_data['auth_db']
        return AuthDBConfig(host=auth_db['host'],
                            username=auth_db['username'],
                            password=auth_db['password'],
                            basename=auth_db['basename'],
                            port=auth_db['port'])

    def get_cn_data_db_config(self) -> DataDBConfig:
        cn_data_db = self._config_data['cn_data_db']
        return DataDBConfig(name='China database',
                            host=cn_data_db['host'],
                            username=cn_data_db['username'],
                            password=cn_data_db['password'],
                            basename=cn_data_db['basename'],
                            port=cn_data_db['port'],
                            timezone_offset_min=cn_data_db['time_zone_offset_min'])

    def get_us_data_db_config(self) -> DataDBConfig:
        us_data_db = self._config_data['us_data_db']
        return DataDBConfig(name='US database',
                            host=us_data_db['host'],
                            username=us_data_db['username'],
                            password=us_data_db['password'],
                            basename=us_data_db['basename'],
                            port=us_data_db['port'],
                            timezone_offset_min=us_data_db['time_zone_offset_min'])

    def get_log_config(self) -> LogConfig:
        log = self._config_data['log']
        std_out = log['std_out']
        level_str = log['level'].lower()
        level = logging.NOTSET
        if level_str == 'debug':
            level = logging.DEBUG
        elif level_str == 'info':
            level = logging.INFO
        elif level_str == 'warn' or level_str == 'warning':
            level = logging.WARNING
        elif level_str == 'error':
            level = logging.ERROR
        elif level_str == 'fatal':
            level = logging.FATAL
        local_file = None
        logentries_token = None
        if 'local_file' in log:
            local_file = log['local_file']
        if 'logentries_token' in log:
            logentries_token = log['logentries_token']
        return LogConfig(std_out=std_out, level=level, local_file=local_file, logentries_token=logentries_token)
