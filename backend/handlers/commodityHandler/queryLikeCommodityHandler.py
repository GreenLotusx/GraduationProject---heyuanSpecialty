from app import config
from handlers.commodityHandler.baseHandler import BaseHandler

class QueryLikeCommodityHandler(BaseHandler):
    def get(self):
        keyword = self.get_argument('keyword')
        strKyeWord = '%'
        for x in keyword:
            strKyeWord += x
            strKyeWord += '%'
        commodityData = self.db.query_like(likeField='ci_title', likeValue=strKyeWord,table="tab_com_infos")
        if commodityData:
            ManyData = []
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
                ManyData.append(data)
            retData = self._returnData(True,ManyData)
        elif commodityData == 0:
            retData = self._returnData(True,[])
        else:
            retData = self._returnData(False,'error_db')
        self.write(retData)