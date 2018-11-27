from handlers.commodityHandler.baseHandler import BaseHandler

class DeleteCommodityHandler(BaseHandler):
    def get(self):
        if self.session.data.get('identity') <= 1:
            cid = str(self.get_argument('cid'))                                                    #删除某商品前，必须先删除用户表里面对应的商品
            wfv = " ci_id = " + cid
            wfvOrd = " oi_cid = " + cid
            resultOrder = self.db.delete(table="tab_order_infos",whereFieldValue=wfvOrd)
            if resultOrder:
                result = self.db.delete(table='tab_com_infos',whereFieldValue=wfv)
                if result:
                    retData = self._returnData(True,'商品删除成功')
                else:
                    retData = self._returnData(False, 'error_db')
            else:
                retData = self._returnData(False,'error_db')
        else:
            retData = self._returnData(False,'error_identity')
        self.write(retData)