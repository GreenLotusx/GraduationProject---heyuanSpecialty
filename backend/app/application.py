import tornado.web
from db.mysqlHandler import DBHandler
from db.redisHandler import  RedisHandler

class Application(tornado.web.Application):
    """重写Application类，添加上数据库操作实例类"""
    def __init__(self,*args,**kwargs):
        super(Application,self).__init__(*args,**kwargs)
        self.db = DBHandler()
        self.redis = RedisHandler()