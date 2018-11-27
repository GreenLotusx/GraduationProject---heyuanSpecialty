from util.userPic import UserPic
from util.loginDecorator import decorator
from handlers.userhandler.baseHandler import BaseHandler

class SetUserInfosHandler(BaseHandler):
    @decorator
    def post(self, *args, **kwargs):
        id = self.session.data.get('id')
        parameter = eval(self.get_argument('parameter',''))
        fileData = self.request.files.get('file',None)
        print('传入参数：',end='')
        print(parameter)
        wfv = "ui_id = " + str(id)
        sex = self._getSex(parameter['sex'])
        sfv = " ui_name = '" +parameter['userName'] + "',ui_mailbox = '"+parameter['mailBox' ]+ "',ui_sex = " + sex
        if fileData:
            file = UserPic(fileData)
            path = file.getUsePic()
            sfv += ",ui_pic = '" + path +"'"
        result = self.db.update(whereFieldValue=wfv,setFieldValue= sfv,table='tab_user_infos')
        if result:
            self.session.data['name'] = parameter['userName']
            self.session.save()
            retData = self._returnData(True,'资料修改成功')
        else:
            retData = self._returnData(False,'error_db')
        self.write(retData)
