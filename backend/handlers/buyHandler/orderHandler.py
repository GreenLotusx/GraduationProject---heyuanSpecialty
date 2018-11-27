import time
from util.loginDecorator import decorator
from handlers.buyHandler.baseHandler import BaseHandler

class OrderHandler(BaseHandler):
    @decorator
    def post(self):
        uid = str(self.session.data.get('id'))
        cidList = self.json_args.get('cidList')
        orderFrom = self.json_args.get('orderFrom')
        print('这为：',end='')
        print(self.json_args)
        if cidList:
            comList = []
            orderNumber = int(time.time())
            result = True
            if orderFrom == 'cart':
                for item in cidList:
                    wfv = " oi_uid = " + uid + " and oi_cid = " + item[0] + " and oi_state = 0"
                    sfv = " oi_number = " + str(orderNumber) + ", oi_num = "+ item[1] +", oi_state = 1"
                    resultItem = self.db.update(whereFieldValue=wfv,setFieldValue=sfv,table="tab_order_infos")
                if resultItem == False:
                    result = False
            else:
                list = {
                    'oi_uid': uid,
                    'oi_cid': cidList[0][0],
                    'oi_num':cidList[0][1],
                    'oi_state': 1,
                    'oi_price': 0,
                    'oi_number':orderNumber
                }
                print('要添加的集合未：')
                print(list)
                result = self.db.add(table='tab_order_infos', **list)

            if result:
                retData = self._returnData(True,{'orderNum':orderNumber})
            else:
                retData = self._returnData(False,'error_db')
        else:
            retData = self._returnData(False,'error_parameter')
        self.write(retData)