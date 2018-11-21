import os, shutil
import logging
from model.config.loader import BasicConfigLoader
from model.db.manager import AuthDBManager, DataDBManager
from model.oss.manager import OssManager

logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(levelname)s]%(filename)s:%(lineno)s - %(message)s')
logger = logging.getLogger()


# 数据库
class DatabaseHandle:
    def __init__(self):
        self.__loader = BasicConfigLoader('config/config_test.yaml')
        self.__auth_db = AuthDBManager(self.__loader.get_auth_db_config())
        self.__oss_auth = OssManager(self.__loader.get_oss_config())
        self.__record_list = []
        self.__filtered_record = []

    def get_test_db_len(self):  # 获取列表长度
        self.__record_list = self.__auth_db.get_record_some_file()
        self.__filtered_record = list(filter(lambda record: record.user_id == 343, self.__record_list))
        return len(self.__filtered_record)

    def get_record_id(self, index: int):  # 获取当前id
        record = self.__filtered_record[index]
        # record_id_str = str(record.record_id)
        return record.record_id

    def get_user_id(self, index: int):  # 获取用户id
        record = self.__filtered_record[index]
        return record.user_id

    def get_test_file_info(self, index: int):  # 获取analyzed信息
        record = self.__filtered_record[index]
        return record.analyzed_file_name

    def get_version(self, index: int):  # 通过版本判断晚睡和小睡
        record = self.__filtered_record[index]
        mark = record.version[-6:]
        if mark == '.0.0.1':
            return 'sleep.1.0'
        return 'nap.1.0'

    def get_start_time(self, index: int):  # 获取特定格式的时间
        record = self.__filtered_record[index]
        date = record.start_time
        return date.strftime("%Y-%m-%d-%H-%M-%S")

    def get_store_oss_end_point(self, index: int):
        record = self.__record_list[index]
        return record.store

    def update_record(self, report_version: str, report_file_name: str, record_id: int):
        record = self.__auth_db.update_record_report(report_version, report_file_name, record_id)
        return record

    def commit(self):
        return self.__auth_db.commit()


# oss管理
class OssHandler:
    def __init__(self):
        self.__loader = BasicConfigLoader('config/config_test.yaml')
        self.__oss_auth = OssManager(self.__loader.get_oss_config())

    def download_file(self, file_dir: str, local_dir: str):
        if self.__oss_auth.object_exists(file_dir):
            self.__oss_auth.download(oss_filename=file_dir, local_filename=local_dir)
            return True

        return False

    def upload_file(self, local_dir: str, oss_dir: str):
        return self.__oss_auth.upload(local_filename=local_dir, oss_filename=oss_dir)


def main():
    print('-----------------------Reprot----------------------')
    analyzed_file_name = os.getcwd() + '/build/tmp.analyzed'
    report_loc_name = os.getcwd() + '/build/tmp.report'
    faild_file_dir = os.getcwd() + '/build/failed/'
    if not os.path.exists(faild_file_dir):
        os.mkdir(faild_file_dir)

    db_handler = DatabaseHandle()
    oss_handler = OssHandler()
    test_db_len = db_handler.get_test_db_len()  # 获取到的数据个数
    transfer_failed = 0  # 统计失败个数
    failed_id_store = []  # 失败的id集合

    for db_index in range(test_db_len):
        file_info = db_handler.get_test_file_info(index=db_index)  # analyzed 文件地址
        record_id = db_handler.get_record_id(db_index)  # 数据编号
        start_time = db_handler.get_start_time(db_index)
        user_id = db_handler.get_user_id(db_index)
        file_type = file_info[-8:]
        if file_type == 'analyzed':  # 判断是否为analyzed结尾
            if oss_handler.download_file(file_info, analyzed_file_name):  # 下载文件
                transfer = os.system('./build/ReportFileFormatter -i build/tmp.analyzed -f')  # 运行批处理
                if transfer != 0:
                    transfer_failed += 1
                    failed_id_store.append(record_id)
                    print('transfer failed, in id: %d\r\n' % record_id)
                    try:
                        tmp_dir = faild_file_dir + 'tmp.analyzed'
                        if os.path.exists(tmp_dir):
                            os.remove(tmp_dir)
                        shutil.move(analyzed_file_name, faild_file_dir)
                        os.rename(tmp_dir, faild_file_dir + start_time + '.analyzed')

                    except Exception as e:
                        print(e)
                        print('rename file fail\r\n')

                else:
                    report_version = db_handler.get_version(db_index)
                    report_oss_name = 'report/' + str(user_id) + '/' + start_time + '.report'
                    # upload = oss_handler.upload_file(report_loc_name, report_oss_name)
                    # if upload.status == 200:
                    #     update = db_handler.update_record(report_version, report_oss_name, record_id)
                    #     if update < 0:
                    #         transfer_failed += 1
                    #         print('update sql failed, in id: %d\r\n' % record_id)
                    #         break
                    # else:
                    #     transfer_failed += 1
                    #     print('upload failed, in id: %d\r\n' % record_id)
                    #     break
    # if test_db_len - transfer_failed > 0:
    #     db_handler.commit()

    print(u'Total : %d,   Failed : %d\r\n' % (test_db_len, transfer_failed))# 8364 6315 1113


if __name__ == '__main__':
    main()
