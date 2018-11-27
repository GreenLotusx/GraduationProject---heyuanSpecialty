import hashlib
import logging
from app import config
from util.session import Session
from handlers.baseHandler import BaseHandler

class LoginHandler(BaseHandler):
    def post(self, *args, **kwargs):
        userName = self.json_args.get("username")
        passWord = self.json_args.get("password") + config.sha_salt
        sha256 = hashlib.sha256()
        sha256.update(passWord.encode(encoding='utf-8'))
        passWordEncryption = sha256.hexdigest().lower()
        userInfos = self.redis.get(userName)
        login = False
        identity = 3
        if userInfos:                #redis中有该用户
            userData = eval(self.redis.get(userName))
            if userData.get('ui_salt') == passWordEncryption:                     #判断redis中密码哈希值和传入的密码哈希值是否一致
                login = True
                user_name = userData.get('ui_name')
                identity = userData.get('ui_identity')
                try:
                    self.session = Session(self)
                    self.session.data['id'] =userData.get('ui_id')
                    self.session.data['name'] = userData.get('ui_name')
                    self.session.data['identity'] = userData.get('ui_identity')
                    self.session.save()
                except Exception as e:
                    logging.error(e)
        else:                                                         #redis中没有该用户,转到mysql查询
            userData = self.db.query_one(whereFieldValue="ui_number = '" + userName + "'", table='tab_user_infos')
            if userData:
                if userData[0]['ui_salt'] == passWordEncryption:                    #登陆成功
                    print('登陆成功')
                    login = True
                    identity = userData[0].get('ui_identity')
                    user_name = userData[0].get('ui_name')
                    try:
                        self.session = Session(self)
                        self.session.data['id'] = userData[0].get('ui_id')
                        self.session.data['name'] = userData[0].get('ui_name')
                        self.session.data['identity'] = userData[0].get('ui_identity')
                        self.session.save()
                    except Exception as e:
                        logging.error(e)
                else:
                    login = False
                result = str(userData[0])
                self.redis.set(userName,result)
            else:                                                                                                       #账户或密码错误
                login = False
        if login:
            content = {
                'msg':'登陆成功',
                'name':user_name,
                'identity':identity
            }
            retData = self._returnData(True,content)
        else:
            retData = self._returnData(False, 'error_login')
        self.write(retData)