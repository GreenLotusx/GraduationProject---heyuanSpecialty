import os
import pymysql

current_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))+'/frontend'
log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),"logs/log")

mysql_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'Lqq724512',
    'db': 'db_gp',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

redis_config = {
    'host': '127.0.0.1',
    'port': 6379
}

Session_expires_time = 43200                       #session有效期(秒)

sha_salt = 'c02e1c599b52106c7e57ce77897524abd2318a4956a5ec72d050d11123008ba9'

#静态文件夹路径
# filePath = '/static/'
filePath = os.path.join(current_path, "static/"),

#用户头像、商品图片路径
uPicPath = '/static/images/userPic/'
cPicPath = '/static/images/commodityPic/'



usePicSize = (120,120)                                          ##用户头像处理后尺寸，分辨率

settings = {                                                           ##项目配置
    "static_path":filePath[0],
    "cookie_secret":"cHJvdWRib3lncmVlbmxvdHVzeA==",
    "xsrf_cookies":True,
    "autoescape":None,
    "login_url": "/login",
    "debug": False
}
