import time
from util.loginDecorator import decorator
from handlers.buyHandler.baseHandler import BaseHandler

class AddCartHandler(BaseHandler):
    @decorator
    def get(self, *args, **kwargs):
        uid = self.session.data.get('id')
        try:
            cid = self.get_argument('cid')
            num = self.get_argument('num')
        except Exception as e:
            return self.write(self._returnData(False,'error_parameter'))
        else:
            checkData = self.__checkRepeat(uid, cid)
            if checkData:
                print('有重复的')
                retData = self.__updateDB(uid,cid,checkData + int(num))
            else:
                print("没有重复的")
                retData = self.__addDB(uid,cid,num)
        self.write(retData)

    def __addDB(self,uid,cid,num):
        """把数据插入到数据库"""
        list = {
            'oi_uid': uid,
            'oi_cid': cid,
            'oi_state': 0,
            'oi_price': 0,
            'oi_num':num,
            'oi_number': int(time.time())
        }
        result = self.db.add(table='tab_order_infos', **list)
        if result:
            retData = self._returnData(True, '成功添加到购物车')
        else:
            retData = self._returnData(False, 'error_db')
        return retData

    def __checkRepeat(self,uid,cid):
        """检查需要插入的商品是否已经在该用户购物车"""
        wfv = " oi_uid = " + str(uid) + " and oi_cid = " + str(cid) + " and oi_state = 0"
        checkData = self.db.query_one(whereFieldValue=wfv,table="tab_order_infos")
        print(checkData)
        if checkData:
            return checkData[0]['oi_num']
        else:
            return False

    def __updateDB(self,uid,cid,num):
        """该用户购物车中有该商品,执行更新商品数量操作"""
        wfv = " oi_uid = " + str(uid) + " and oi_cid = " + str(cid) + " and oi_state = 0"
        sfv = " oi_num = " + str(num)
        print(wfv)
        print(sfv)
        updateData = self.db.update(whereFieldValue=wfv,setFieldValue=sfv,table="tab_order_infos")
        if updateData:
            retData = self._returnData(True,'成功添加到购物车')
        else:
            retData = self._returnData(False, 'error_db')
        return retData