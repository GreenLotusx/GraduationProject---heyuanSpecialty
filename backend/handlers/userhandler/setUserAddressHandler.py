from util.loginDecorator import decorator
from handlers.userhandler.baseHandler import BaseHandler

class SetUserAddressHandler(BaseHandler):
    @decorator
    def post(self):
        uid = str(self.session.data.get('id'))
        addressee = self.json_args.get('addressee')
        address = self.json_args.get('address')
        phone = self.json_args.get('phoneNumber')
        zipCode = self.json_args.get('zipCode')
        setAddress = address + '  ' + addressee + '(收)  ' + phone + '  ' + zipCode
        result = self.db.update(whereFieldValue= " ui_id = " + uid, setFieldValue=" ui_address = '" + setAddress + "'" , table='tab_user_infos')
        if result:
            retData = self._returnData(True,'用户地址修改成功')
        else:
            retData = self._returnData(False,'error_db')
        self.write(retData)
