from typing import List
import pymysql
import datetime
from model.config.config import AuthDBConfig, DataDBConfig
from .data_type import User, Record_All, Gender, AlarmClockMode, Server, UserQuality, Record_Some


class AuthDBManager:
    def __init__(self, auth_db_config: AuthDBConfig):
        self.__auth_db_config = auth_db_config
        self.__auth_db = pymysql.connect(host=auth_db_config.host,
                                         user=auth_db_config.username,
                                         password=auth_db_config.password,
                                         db=auth_db_config.basename,
                                         charset='utf8',
                                         use_unicode=True)

    def __del__(self):
        self.__auth_db.close()

    @property
    def config(self) -> AuthDBConfig:
        return self.__auth_db_config

    @staticmethod
    def __get_user_sql_pattern() -> str:
        return ' id, email, phone, email_verified, phone_verified, social_weixin, social_weibo, social_qq,' \
               ' social_facebook, social_twitter, social_google, server_id, open_client_id, open_user_id, name,' \
               ' gender, birth, height, weight, subscribe_email, deleted_at, created_at, updated_at'

    @staticmethod
    def __get_record_some_sql_pattern() -> str:
        res = 'id, user_id, start_time, version, store, analyzed_file_name, updated_at'
        return res

    def get_record_some_file(self) -> List[Record_Some]:
        res = []

        with self.__auth_db.cursor() as cursor:
            sql = 'select ' + self.__get_record_some_sql_pattern() + \
                  ' from naptime_records where analyzed_file_name IS NOT NULL and report_file_name is null'
            cursor.execute(sql)
            for row in cursor:
                res.append(Record_Some(
                    record_id=row[0],
                    user_id=row[1],
                    start_time=row[2],
                    version=row[3],
                    store=row[4],
                    analyzed_file_name=row[5],
                    updated_at=row[6]
                    # record_version=row[6],
                    # record_file_name=row[7]
                )
                )

        return res

    def update_record_report(self, report_version: str, report_file_name: str, report_id: int) -> bool:
        with self.__auth_db.cursor() as cursor:
            sql = "update naptime_records set report_version='%s' , report_file_name='%s' where id=%d" \
                  % (report_version, report_file_name, report_id)

            result = cursor.execute(sql)
            return result

    def commit(self):
        return self.__auth_db.commit()

    def execute_sql(self, sql: str):
        res = []
        with self.__auth_db.cursor() as cursor:
            cursor.execute(sql)
            for row in cursor:
                res.append(row)
            self.__auth_db.commit()
        return res


class DataDBManager:
    def __init__(self, data_db_config: DataDBConfig):
        self.__data_db_config = data_db_config
        self.__data_db = pymysql.connect(host=data_db_config.host,
                                         user=data_db_config.username,
                                         password=data_db_config.password,
                                         db=data_db_config.basename,
                                         charset='utf8',
                                         use_unicode=True)

    def __del__(self):
        self.__data_db.close()

    @property
    def config(self) -> DataDBConfig:
        return self.__data_db_config

    @staticmethod
    def __get_record_sql_pattern() -> str:
        res = 'id, user_id, start_time, duration, sober_duration, sleep_light_duration,' \
              'sleep_heavy_duration, sleep_degree, relax_degree, score, musics, alarm_clock_mode,' \
              'user_quality, device_id, version, store, raw_file_name, analyzed_file_name, deleted_at,' \
              'created_at, updated_at'
        return res

    @staticmethod
    def __get_record_some_sql_pattern() -> str:
        res = 'id, user_id, start_time, store, analyzed_file_name, updated_at'
        return res

    def get_record_some_file(self) -> List[Record_Some]:
        res = []

        with self.__data_db.cursor() as cursor:
            sql = 'select ' + self.__get_record_some_sql_pattern() + \
                  ' from naptime_records where analyzed_file_name IS NOT NULL and report_file_name is null'
            cursor.execute(sql)
            for row in cursor:
                res.append(Record_Some(
                    record_id=row[0],
                    user_id=row[1],
                    start_time=row[2],
                    store=row[3],
                    analyzed_file_name=row[4],
                    updated_at=row[5]
                    # record_version=row[6],
                    # record_file_name=row[7]
                )
                )

        return res

    # def update_record

    def execute_sql(self, sql: str):
        res = []
        with self.__data_db.cursor() as cursor:
            cursor.execute(sql)
            for row in cursor:
                res.append(row)
            self.__data_db.commit()
        return res
