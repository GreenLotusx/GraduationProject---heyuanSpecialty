from app import config
from util.loginDecorator import decorator
from handlers.buyHandler.baseHandler import BaseHandler

class QueryCartHandler(BaseHandler):
    @decorator
    def get(self, *args, **kwargs):
        uid = self.session.data.get('id')
        sql = "select * from tab_order_infos right join tab_com_infos on oi_cid = ci_id where oi_uid = " + str(uid) + " and oi_state = 0"
        cartData = self.db.query_custom(sql)
        cartDataList = []
        if cartData:
            for item in  cartData:
                data = {
                    'num': item['oi_num'],
                    'id':item['ci_id'],
                    'title':item['ci_title'],
                    'infos':item['ci_infos'],
                    'oprice':self._getMoney(item['ci_oprice']),
                    'nprice':self._getMoney(item['ci_nprice']),
                    'img':config.cPicPath + item['ci_img'],
                    'specifications':item['ci_specifications'],
                    'sumprice':self._getMoney(int(item['oi_num']) * int(item['ci_nprice']))
                }
                cartDataList.append(data)
            retData = self._returnData(True,cartDataList)
        else:
            retData = self._returnData(True,[])
        self.write(retData)