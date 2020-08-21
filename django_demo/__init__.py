import logging.config
import pymysql
from django_demo.utils.log_handler import get_log_conf
from django_demo.utils.redis_pool import RedisPool
from django_demo.utils.thread_pool import ThreadPool


# mysql配置
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()  # 使用pymysql代替mysqldb连接数据库

# 日志配置
login_dict = get_log_conf()
logging.config.dictConfig(login_dict)
logger = logging.getLogger('web_info')

# 主线程中的全局redis链接池
# global_redis_pool的生命周期是Django主线程运行的生命周期
global_redis_pool = RedisPool()

# 主线程中的全局线程池
# global_thread_pool的生命周期是Django主线程运行的生命周期
global_thread_pool = ThreadPool()