from redis import *
from app.config import redis_config

class RedisHandler(object):
    def __init__(self):
        self.__redis = StrictRedis(**redis_config)

    def set(self,key,value):
        self.__redis.set(key,value)

    def setex(self,key,time,value):
        self.__redis.setex(key,time,value)

    def get(self,key):
        return self.__redis.get(key)

    def delete(self,key):
        self.__redis.delete(key)