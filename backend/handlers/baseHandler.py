import json
import tornado.web
from tornado.web import RequestHandler
from util.constants import ERROR_CODE,ERROR_MSG
from util.session import Session

class BaseHandler(RequestHandler):
    """handler基类"""

    @property
    def db(self):
        return self.application.db

    @property
    def redis(self):
        return self.application.redis

    def prepare(self):
        self.xsrf_token
        if self.request.headers.get("Content-Type","").startswith("application/json"):
            self.json_args = json.loads(self.request.body)
        else:
            self.json_args = None

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        pass

    def initialize(self):
        pass

    def on_finish(self):
        pass

    def get_current_user(self):
        self.session = Session(self)
        return self.session.data

    def _returnData(self,state,data=None):
        """
        生成返回数据,传入状态(True或False),还有就是具体数据，
        通常为list或dict,如果状态为false,则传入常量中定义的具体错误
        """
        content = {}
        if state == True:
            if data:
                content = {
                    'error':ERROR_CODE['success'],
                    'data':data,
                    'msg':ERROR_MSG['success']
                }
            else:
                content = {
                    'error': ERROR_CODE['success'],
                    'msg': ERROR_MSG['success']
                }
        else:
            content = {
                'error':ERROR_CODE.get(data),
                'msg':ERROR_MSG.get(data)
            }
        return content

# class StaticFileHandler(tornado.web.StaticFileHandler):
#         def __init__(self,*args,**kwargs):
#             super(StaticFileHandler,self).__init__(*args,**kwargs)
#             self.xsrf_token