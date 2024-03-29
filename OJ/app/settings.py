import os

environ = os.environ
# PROJECT_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.getcwd()
TEMPLATE_FOLDER = os.path.join(PROJECT_PATH, "templates")
STATIC_FOLDER = os.path.join(PROJECT_PATH, "static")
DEBUG = True  # open debug /or hot restart

# ****** 上传配置
UPLOAD_FOLDER = '/tmp/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'sql'}

# SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

# ****** MySQL 配置
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'.format(
    user=environ.get('DB_USER', 'DB_USER'),
    password=environ.get('DB_PASS', 'DB_PASS'),
    host=environ.get('DB_HOST', '127.0.0.1'),
    port=environ.get('DB_PORT', 3306),
    database=environ.get('DB_NAME', 'DB_NAME'))
# # SQLALCHEMY_POOL_SIZE = 15  # 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
# # SQLALCHEMY_POOL_TIMEOUT = 10  # 指定数据库连接池的超时时间。默认是 10。
# # SQLALCHEMY_POOL_RECYCLE = 60 * 60 * 2  # 自动回收连接的秒数。
# # SQLALCHEMY_MAX_OVERFLOW = 0  # 控制在连接池达到最大值后可以创建的连接数。
# SQLALCHEMY_POOL_SIZE = 30  # 数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。
# SQLALCHEMY_POOL_TIMEOUT = 10  # 指定数据库连接池的超时时间。默认是 10。
# SQLALCHEMY_POOL_RECYCLE = 60 * 60 * 2  # 自动回收连接的秒数。
# SQLALCHEMY_MAX_OVERFLOW = 20  # 控制在连接池达到最大值后可以创建的连接数。


REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', 'REDIS_PASSWORD')
REDIS_DB = os.environ.get('REDIS_DB', '0')
if REDIS_PASSWORD:
    RESULT_BACKEND = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
    BROKER_URL = f'redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
else:
    RESULT_BACKEND = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'
    BROKER_URL = f'redis://{REDIS_PORT}/{REDIS_DB}'

HOST = environ.get('HOST', '0.0.0.0')
PORT = environ.get('PORT', 16808)

JUDGER_SERVER = 'http://{judger_host}:{judger_port}/'.format(
    judger_host=environ.get('JUDGER_HOST', '127.0.0.1'),
    judger_port=environ.get('JUDGER_PORT', '16358'),
)
JUDGER_TOKEN = environ.get('JUDGER_TOKEN', '123456')

# middleware settings
CHECKLOGIN_EXCLUDE_PATH = [
    '/api/user/register',
    '/api/user/login',
    '/api/submission/status',
    '/api/contest/recent',
    '/api/contest/all',
    '/api/contest/detail',
    '/api/contest/announcements',
    '/api/problem/hot',
    '/api/problem/all',
    '/api/problem/detail',
    '/api/admin/sys/qdu/import',
    '/docs',
    '/openapi.json',
]

AES_KEY = environ.get('AES_KEY', 'Your_AES_KEY')
AES_KEY = AES_KEY.ljust(16)

TEST_CASE_DIR = ''
