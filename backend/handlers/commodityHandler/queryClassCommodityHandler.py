from app import config
from handlers.commodityHandler.baseHandler import BaseHandler

class QueryClassCommodityHandler(BaseHandler):
    def get(self):
        clsid = self.get_argument('clsid')
        commodityData = self.db.query_many(whereFieldValue=' where ci_class = ' + str(clsid))
        if commodityData:
            ManyData = []
            for item in commodityData:
                data = {
                    'id': item['ci_id'],
                    'img': config.cPicPath + item['ci_img'],
                    'title': item['ci_title'],
                    'freight': self._getMoney(item['ci_freight']),
                    'price': self._getMoney(item['ci_nprice']),
                    'sales': item['ci_sales'],
                    'class': self._getClass(item['ci_class']),
                    'ordprice': self._getMoney(item['ci_oprice']),
                    'specifications': item['ci_specifications']
                }
                ManyData.append(data)
            retData = self._returnData(True,ManyData)
        else:
            retData = self._returnData(False,'error_db')
        self.write(retData)