from util.loginDecorator import decorator
from handlers.buyHandler.baseHandler import BaseHandler

class DeleteCartHandler(BaseHandler):
    @decorator
    def get(self):
        uid = self.session.data.get('id')
        try:
            cid = self.get_argument('cid')
            wfv = " oi_uid = " + str(uid) + " and oi_cid = " + str(cid) + "and oi_state = 0"
        except Exception:
            print('异常')
            wfv = " oi_uid = " + str(uid) + " and oi_state = 0"
        result = self.db.delete(whereFieldValue=wfv,table="tab_order_infos")
        if result:
            retData = self._returnData(True,'商品删除成功')
        else:
            retData = self._returnData(False,'error_db')
        self.write(retData)