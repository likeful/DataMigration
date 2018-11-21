import datetime
from enum import Enum


class AlarmClockMode(Enum):
    NONE = 0
    SMART = 1
    MANUAL = 2


class Gender(Enum):
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2


class UserQuality(Enum):
    DEFAULT = 0
    VERY_POOR = 1
    POOR = 2
    FINE = 3
    GOOD = 4
    VERY_GOOD = 5


class Server(Enum):
    CN = 1
    US = 2


class Record_Some:
    def __init__(self,
                 record_id: int=None,
                 user_id: int=None,
                 start_time: datetime.datetime=None,
                 version: str=None,
                 store: str=None,
                 analyzed_file_name: str=None,
                 updated_at: datetime.datetime = None
                 # record_version: str=None,
                 # record_file_name=None
                ):
        self.__record_id = record_id
        self.__user_id = user_id
        self.__start_time = start_time
        self.__version = version
        self.__store = store
        self.__analyzed_file_name = analyzed_file_name
        self.__updated_at = updated_at
        # self.__record_version = record_version
        # self.__record_file_name = record_file_name

    @property
    def record_id(self) -> int:
        return self.__record_id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def start_time(self) -> datetime.datetime:
        return self.__start_time

    @property
    def version(self) -> str:
        return self.__version

    @property
    def store(self) -> str:
        return self.__store

    @property
    def analyzed_file_name(self) -> str:
        return self.__analyzed_file_name

    @property
    def updated_at(self) -> datetime.datetime:
        return self.__updated_at

    # @property
    # def store(self) -> str:
    #     return self.__record_version
    #
    # @property
    # def raw_file_name(self) -> str:
    #     return self.__record_file_name


class Record_All:
    def __init__(self,
                 record_id: int=None,
                 user_id: int=None,
                 start_time: datetime.datetime=None,
                 duration: int=None,
                 sober_duration: int=None,
                 sleep_light_duration: int=None,
                 sleep_heavy_duration: int=None,
                 sleep_degree: int=None,
                 relax_degree: int=None,
                 score: int=None,
                 musics: str=None,
                 alarm_clock_mode: AlarmClockMode=None,
                 user_quality: UserQuality=None,
                 device_id: str=None,
                 version: str=None,
                 store: str=None,
                 raw_file_name: str=None,
                 analyzed_file_name: str=None,
                 deleted_at: datetime.datetime=None,
                 created_at: datetime.datetime=None,
                 updated_at: datetime.datetime=None,
                 record_version: str=None,
                 record_file_name=None):
        self.__record_id = record_id
        self.__user_id = user_id
        self.__start_time = start_time
        self.__duration = duration
        self.__sober_duration = sober_duration
        self.__sleep_light_duration = sleep_light_duration
        self.__sleep_heavy_duration = sleep_heavy_duration
        self.__sleep_degree = sleep_degree
        self.__relax_degree = relax_degree
        self.__score = score
        self.__musics = musics
        self.__alarm_clock_mode = alarm_clock_mode
        self.__user_quality = user_quality
        self.__device_id = device_id
        self.__version = version
        self.__store = store
        self.__raw_file_name = raw_file_name
        self.__analyzed_file_name = analyzed_file_name
        self.__deleted_at = deleted_at
        self.__created_at = created_at
        self.__updated_at = updated_at
        self.__record_version = record_version
        self.__record_file_name = record_file_name


    @property
    def record_id(self) -> int:
        return self.__record_id

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def start_time(self) -> datetime.datetime:
        return self.__start_time

    @property
    def duration(self) -> int:
        return self.__duration

    @property
    def sober_duration(self) -> int:
        return self.__sober_duration

    @property
    def sleep_light_duration(self) -> int:
        return self.__sleep_light_duration

    @property
    def sleep_heavy_duration(self) -> int:
        return self.__sleep_heavy_duration

    @property
    def sleep_degree(self) -> int:
        return self.__sleep_degree

    @property
    def relax_degree(self) -> int:
        return self.__relax_degree

    @property
    def score(self) -> int:
        return self.__score

    @property
    def musics(self) -> str:
        return self.__musics

    @property
    def alarm_clock_mode(self) -> AlarmClockMode:
        return self.__alarm_clock_mode

    @property
    def user_quality(self) -> UserQuality:
        return self.__user_quality

    @property
    def device_id(self) -> str:
        return self.__device_id

    @property
    def version(self) -> str:
        return self.__version

    @property
    def store(self) -> str:
        return self.__store

    @property
    def raw_file_name(self) -> str:
        return self.__raw_file_name

    @property
    def analyzed_file_name(self) -> str:
        return self.__analyzed_file_name

    @property
    def deleted_at(self) -> datetime.datetime:
        return self.__deleted_at

    @property
    def created_at(self) -> datetime.datetime:
        return self.__created_at

    @property
    def updated_at(self) -> datetime.datetime:
        return self.__updated_at

    @property
    def store(self) -> str:
        return self.__record_version

    @property
    def raw_file_name(self) -> str:
        return self.__record_file_name


class User:
    def __init__(self,
                 user_id: int=None,
                 email: str=None,
                 phone: str=None,
                 email_verified: bool=None,
                 phone_verified: bool=None,
                 social_weixin: str=None,
                 social_weibo: str=None,
                 social_qq: str=None,
                 social_facebook: str=None,
                 social_twitter: str=None,
                 social_google: str=None,
                 server_id: Server=None,
                 open_client_id: int=None,
                 open_user_id: int=None,
                 name: str=None,
                 gender: Gender=None,
                 birth: datetime.date=None,
                 height: int=None,
                 weight: float=None,
                 subscribe_email: str=None,
                 deleted_at: datetime.datetime=None,
                 created_at: datetime.datetime=None,
                 updated_at: datetime.datetime=None):
        self.__user_id = user_id
        self.__email = email
        self.__phone = phone
        self.__email_verified = email_verified
        self.__phone_verified = phone_verified
        self.__social_weixin = social_weixin
        self.__social_weibo = social_weibo
        self.__social_qq = social_qq
        self.__social_facebook = social_facebook
        self.__social_twitter = social_twitter
        self.__social_google = social_google
        self.__server_id = server_id
        self.__name = name
        self.__gender = gender
        self.__birth = birth
        self.__height = height
        self.__weight = weight
        self.__subscribe_email = subscribe_email
        self.__deleted_at = deleted_at
        self.__created_at = created_at
        self.__updated_at = updated_at

    @property
    def user_id(self)->int:
        return self.__user_id

    @property
    def email(self) -> str:
        return self.__email

    @property
    def phone(self) -> str:
        return self.__phone

    @property
    def email_verified(self) -> bool:
        return self.__email_verified

    @property
    def phone_verified(self) -> bool:
        return self.__phone_verified

    @property
    def social_weixin(self) -> str:
        return self.__social_weixin

    @property
    def social_weibo(self) -> str:
        return self.__social_weibo

    @property
    def social_qq(self) -> str:
        return self.__social_qq

    @property
    def social_facebook(self) -> str:
        return self.__social_facebook

    @property
    def social_twitter(self) -> str:
        return self.__social_twitter

    @property
    def social_google(self) -> str:
        return self.__social_google

    @property
    def server_id(self) -> Server:
        return self.__server_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def gender(self) -> Gender:
        return self.__gender

    @property
    def birth(self) -> datetime.date:
        return self.__birth

    @property
    def age(self) -> int:
        return datetime.datetime.now().year - self.__birth.year

    @property
    def height(self) -> int:
        return self.__height

    @property
    def weight(self) -> float:
        return self.__weight

    @property
    def subscribe_email(self) -> str:
        return self.__subscribe_email

    @property
    def deleted_at(self) -> datetime.datetime:
        return self.__deleted_at

    @property
    def created_at(self) -> datetime.datetime:
        return self.__created_at

    @property
    def updated_at(self) -> datetime.datetime:
        return self.__updated_at
