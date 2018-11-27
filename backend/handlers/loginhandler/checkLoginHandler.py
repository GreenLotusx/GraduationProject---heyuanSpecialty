from util.loginDecorator import decorator
from util.time import GetTime
from handlers.baseHandler import BaseHandler

class CheckLoginHandler(BaseHandler):
    @decorator
    def get(self):
        data = self.get_current_user()
        data['time'] = GetTime().gettime('年月日&星')
        retData = self._returnData(True,data)
        self.write(retData)
