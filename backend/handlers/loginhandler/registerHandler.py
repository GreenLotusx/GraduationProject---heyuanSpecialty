import time
import hashlib
from app import config
from handlers.baseHandler import BaseHandler

class RegisterHandler(BaseHandler):
    def post(self, *args, **kwargs):
        userNumber = self.json_args.get('useNumber')
        userPwd = self.json_args.get('password')
        userEmail = self.json_args.get('email')
        numSql = "select * from tab_user_infos where ui_number = '" + userNumber + "';"
        emailSql = "select * from tab_user_infos where ui_mailbox = '" + userEmail + "';"
        checkNum = self.db.query_custom(numSql)
        checkEmail = self.db.query_custom(emailSql)
        if checkNum:                                                                      #如果有结果,说明账户重复
            retData = self._returnData(False,'error_useExist')
        if checkEmail:
            retData = self._returnData(False,'error_mailboxExist')
        if not checkNum  and not checkEmail:                                               #都没有结果,说明没有重复
            print('开始插入数据')
            passWord = userPwd + config.sha_salt
            sha256 = hashlib.sha256()
            sha256.update(passWord.encode(encoding='utf-8'))
            passWordEncryption = sha256.hexdigest().lower()
            list = {
                'ui_number': userNumber,
                'ui_name': '会员'+str(int(time.time())),
                'ui_salt': passWordEncryption,
                'ui_mailbox': userEmail
            }
            result = self.db.add(table='tab_user_infos',**list)
            print(result)
            if result:
                retData = self._returnData(True,'用户注册成功')
            else:
                retData = self._returnData(False,'error_failed')
        self.write(retData)