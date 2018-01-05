from os import path
from django.apps import AppConfig
import pymysql

pymysql.install_as_MySQLdb()  # 让pip中的mysql-python支持python3.x

VERBOSE_APP_NAME = u"文章"


def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]


class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME


default_app_config = AppVerboseNameConfig
