from util.loginDecorator import decorator
from handlers.buyHandler.baseHandler import BaseHandler

class PayHandler(BaseHandler):
    @decorator
    def get(self):
        uid = str(self.session.data.get('id'))
        oid = self.get_argument('orderNum')
        sql = "select * from tab_order_infos right join tab_com_infos on oi_cid = ci_id where oi_uid = "+uid+" and oi_state = 1 and oi_number = " + oid
        result = self.db.query_custom(sql)
        if result:
            callback = True
            for item in result:
                price = str(item['ci_nprice'])
            wfv = " oi_uid = " + uid + " and oi_number = " + oid + " and oi_state = 1"
            sfv = " oi_state = 2,oi_price = " + price
            resultItem = self.db.update(whereFieldValue=wfv,setFieldValue=sfv,table="tab_order_infos")              #将订单表该数据
            if resultItem:                  #没有异常，可以更新商品销量
                for item in result:
                    cid = str(item['oi_cid'])
                    num = item['oi_num']
                    wfv = " ci_id = " + cid
                    sfv = " ci_sales = " + str(int(item['ci_sales']) + num)             ##更新对应商品销量
                    uresult = self.db.update(whereFieldValue=wfv,setFieldValue=sfv,table="tab_com_infos")
                    if uresult:
                        print('更新商品销量成功')
                    else:
                        callback = False
            else:
                callback = False
            if callback:
                retData = self._returnData(True,'付款成功')
            else:
                retData = self._returnData(False,'error_db')
        else:
            retData = self._returnData(False,'error_db')
        self.write(retData)