import hashlib
from app import config
from util.loginDecorator import decorator
from handlers.userhandler.baseHandler import BaseHandler

class SetUserPasswordHandler(BaseHandler):
    @decorator
    def post(self):
        uid = str(self.session.data.get('id'))
        ordPwd = str(self.json_args.get('ordPsd'))
        newPwd = str(self.json_args.get('newPsd'))
        print('旧密码为：',end='')
        print(ordPwd)
        print('新密码为：',end='')
        print(newPwd)
        passWord = ordPwd + config.sha_salt
        sha256 = hashlib.sha256()
        sha256.update(passWord.encode(encoding='utf-8'))
        passWordEncryption = sha256.hexdigest().lower()
        userData = self.db.query_one(whereFieldValue="ui_id = '" + uid + "'", table='tab_user_infos')
        if userData:
            if userData[0]['ui_salt'] == passWordEncryption:                            #旧密码正确
                if ordPwd == newPwd:                                                                    ##判断新旧密码是否一致
                    retData = self._returnData(False,'error_noChanged')
                else:
                    passWord = newPwd + config.sha_salt
                    sha256 = hashlib.sha256()
                    sha256.update(passWord.encode(encoding='utf-8'))
                    passWordEncryption = sha256.hexdigest().lower()
                    result = self.db.update(whereFieldValue=" ui_id = " + uid, setFieldValue=" ui_salt = '" + passWordEncryption + "'", table='tab_user_infos')
                    if result:
                        newuserData = self.db.query_one(whereFieldValue="ui_id = '" + uid + "'",table='tab_user_infos')
                        if newuserData:
                            self.redis.set(newuserData[0]['ui_number'], str(newuserData[0]))
                            retData = self._returnData(True,'密码更改成功')
                        else:
                            self.redis.delete(userData[0]['ui_number'])
                            retData = self._returnData(False,'error_server')        ##这种情况是新密码已经更新到数据库,但从数据库取出新的数据存放到redis时出现异常
                    else:
                        retData = self._returnData(False,'error_changePwd')
            else:                                                                                                         #旧密码错误
                retData = self._returnData(False,'error_ordpwd')
        self.write(retData)