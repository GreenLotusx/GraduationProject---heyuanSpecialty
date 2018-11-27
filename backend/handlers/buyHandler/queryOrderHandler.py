from app import config
from util.loginDecorator import decorator
from handlers.buyHandler.baseHandler import BaseHandler

class QueryOrderHandler(BaseHandler):
    @decorator
    def get(self):
        orderNumberList = []
        orderList = []
        uid = str(self.session.data.get('id'))
        sql = "select * from tab_order_infos right join tab_com_infos on oi_cid = ci_id where oi_uid = "+uid+" and oi_state >= 1"
        result = self.db.query_custom(sql)
        if result != False:
            for item in result:
                if item['oi_number'] not in orderNumberList:
                    orderNumberList.append(item['oi_number'])
            for item in orderNumberList:
                orderItemList = {}
                iItem = []
                sumPrice = 0
                print(result)
                for ritem in result:
                    if ritem['oi_number'] == item:
                        if ritem['oi_state'] > 1:
                            sumPrice += (int(ritem['oi_price']) * int(ritem['oi_num']))
                            print('执行到这里1')
                        else:
                            sumPrice += (int(ritem['ci_nprice']) * int(ritem['oi_num']))
                            print('执行到这里2')
                        data = {
                            'cid':ritem['oi_cid'],
                            'price':self._getMoney(ritem['ci_nprice']),
                            'img':config.cPicPath+ritem['ci_img'],
                            'num':ritem['oi_num'],
                            'title':ritem['ci_title'],
                            'specifications':ritem['ci_specifications']
                        }
                        iItem.append(data)
                        orderItemList={
                             'id':ritem['oi_id'],
                            'state': self.__getState(ritem['oi_state']),
                            'number':item,
                            'time':str(ritem['oi_utime']),
                            'cdata':iItem,
                            'sprice':self._getMoney(sumPrice)
                        }
                orderList.append(orderItemList)
            if orderList:
                retData = self._returnData(True,orderList)
            else:
                retData = self._returnData(False,'error_db')
        else:
            retData = self._returnData(True,[])
        self.write(retData)

    def __getState(self,stateNum):
        stateNum = str(stateNum)
        if stateNum == '1':
            return [1,'未支付','待付款','去付款']
        elif stateNum == '2':
            return [2,'已支付','已付款','查看物流']