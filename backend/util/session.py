import uuid
import  logging
import json
from app.config import Session_expires_time

class Session(object):
    """senssion机制实现类"""
    def  __init__(self,request_handler):
        self.redis = request_handler.redis
        self.request_handler = request_handler
        self.session_id = self.request_handler.get_secure_cookie("SESSION_ID")
        if not self.session_id:
            #代表第一次访问，生成一个唯一的id
            self.session_id = uuid.uuid4().hex
            self.data = {}
            request_handler.set_secure_cookie("SESSION_ID",self.session_id)
        else:
            #代表不是第一次访问，从redis中取出
            data = None
            try:
               data = self.redis.get("sess_%s" % self.session_id)
            except Exception as e:
                logging.error(e)
                self.data = {}
                raise e

            if not data:
                #代表session过期
                self.data = {}
            else:
                self.data = json.loads(data)

    def save(self):
        """把session保存到redis中，如果不出错，把该sessionid写入到cookie中"""
        json_data = json.dumps(self.data)
        try:
            self.redis.setex("sess_%s" % self.session_id,Session_expires_time,json_data)
        except Exception as e:
            logging.error(e)
            raise Exception("save session failed")
        else:
            self.request_handler.set_secure_cookie("SESSION_ID",self.session_id)

    def clear(self):
        """登出操作，清除cookie,并删除redis中的数据"""
        result = True
        self.request_handler.clear_cookie("SESSION_ID")
        try:
            self.redis.delete("sess_%s" %(self.session_id))
        except Exception as e:
            logging.error(e)
            result = False
        return result
