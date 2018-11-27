import math
from app import config
from util.constants import PAGE_NUM
from util.loginDecorator import decorator
from handlers.commodityHandler.baseHandler import BaseHandler

class ManyCommodityHandler(BaseHandler):
    @decorator
    def get(self):
        page = 0
        if self.session.data.get('identity') <= 1:
            try:
                number = self.get_argument('number')
            except Exception as e:
                try:
                    page = int(self.get_argument('page'))
                except Exception as e:
                    page = 1
                number = (page - 1) * PAGE_NUM
            print('number为：'+str(number))
            commodityData = self.db.query_many(num=str(number) + ','+ str(PAGE_NUM))
            pageSum = math.ceil(int(self.db.query_sum()[0].get('count(1)')) / PAGE_NUM)
            if commodityData:
                ManyDataItem = []
                for item in commodityData:
                    data = {
                        'id':item['ci_id'],
                        'img':config.cPicPath + item['ci_img'],
                        'title':item['ci_title'],
                        'freight':self._getMoney(item['ci_freight']),
                        'price':self._getMoney(item['ci_nprice']),
                        'sales':item['ci_sales'],
                        'class':self._getClass(item['ci_class']),
                        'ordprice':self._getMoney(item['ci_oprice']),
                        'specifications':item['ci_specifications']
                    }
                    ManyDataItem.append(data)
                ManyData = {
                    'page':page,
                    'page_sum':pageSum,
                    'com_data':ManyDataItem
                }
                print('总页数为：'+str(pageSum))
                retData = self._returnData(True,ManyData)
            else:
                retData = self._returnData(False,'error_query')
        else:
            retData = self._returnData(False,'error_identity')
        self.write(retData)