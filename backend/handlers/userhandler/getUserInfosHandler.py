from app.config import uPicPath
from util.loginDecorator import decorator
from handlers.userhandler.baseHandler import BaseHandler

class UserInfosHandler(BaseHandler):
    @decorator
    def get(self):
        uid = str(self.session.data.get('id'))
        userData = self.db.query_one(whereFieldValue="ui_id = '" + uid + "'", table='tab_user_infos')
        print('查询用户结果：',end='')
        print(userData[0])
        if userData:
            data = {
                'user_name':userData[0].get('ui_name'),
                'user_pic':uPicPath + userData[0].get('ui_pic'),
                'user_sex':self._getSex(userData[0].get('ui_sex')),
                'user_mailbox':userData[0].get('ui_mailbox'),
                'ui_address':self._formatAddress(userData[0].get('ui_address'))
            }
            retData = self._returnData(True,data)
        else:
            retData = self._returnData(False,'error_userinfos')
        print(retData)
        self.write(retData)
