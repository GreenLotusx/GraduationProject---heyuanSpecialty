import time
from app import config
#from tornado import gen
from handlers.commodityHandler.baseHandler import BaseHandler

class QueryIndexHandler(BaseHandler):
    """此处理类为处理首页请求每个类4条数据的类"""
   # @gen.coroutine
    def get(self):
        data = []

       # for i in range(1,5000):
         #yield self.db.query_many(whereFieldValue=" where ci_class = 4 ",num=4)








        for i in range(1,6):
            wfv = " where ci_class = " + str(i)
            itemData = self.db.query_many(whereFieldValue=wfv,num=4)
            ManyData = []
            if itemData != 0:
                for item in itemData:
                    idata = {
                        'id': item['ci_id'],
                        'img': config.cPicPath + item['ci_img'],
                        'title': item['ci_title'],
                        'price': self._getMoney(item['ci_nprice']),
                        'class': [item['ci_class'],self._getClass(item['ci_class'])],
                        'specifications': item['ci_specifications']
                    }
                    ManyData.append(idata)
                data.append(ManyData)
        if data:
            retData = self._returnData(True,data)
        else:
            retData = self._returnData(False,'error_db')
        self.write(retData)

        print('结束请求时间戳：'+str(time.time()))
