from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


BROKER_URL = 'redis://10.248.224.131:6379/2'
CELERY_RESULT_BACKEND = 'redis://10.248.224.131:6379/3'
CELERY_TIMEZONE = 'Asia/Shanghai'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 864000}  # 任务时效 10天
CELERY_ENABLE_UTC = False
CELERY_ACCEPT_CONTENT = ['json', 'pickle', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYD_CONCURRENCY = 16
CELERYD_FORCE_EXECV = True
CELERYD_MAX_TASKS_PER_CHILD = 2
BROKER_POOL_LIMIT = 0  # mysql gone 问题
CELERY_TASK_ALWAYS_EAGER = True


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',   #  指定数据库驱动
        'NAME': 'django_demo',   #  指定的数据库名
        'USER': 'devops',   #  数据库登录的用户名
        'PASSWORD': 'Oqa_rG1j8jLDBNv',  #  登录数据库的密码
        'HOST': '10.248.224.131',
        'PORT': '3306',   #  数据库服务器端口，mysql默认为3306
    }
}


### redis配置
REDIS_CFG = {"host": "10.248.224.131", "port": 6379,"db":6}