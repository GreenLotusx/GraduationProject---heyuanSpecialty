from util.loginDecorator import decorator
from handlers.baseHandler import BaseHandler

class LogoutHandler(BaseHandler):
        @decorator
        def get(self):
            result = self.session.clear()
            if result:
                retData = self._returnData(True, '已经成功注销')
            else:
                retData = self._returnData(False, 'error_logout')
            self.write(retData)