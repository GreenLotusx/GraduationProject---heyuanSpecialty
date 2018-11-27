import logging
from app import config
from handlers.commodityHandler.baseHandler import BaseHandler

class CommodityDataHandler(BaseHandler):
    def get(self):
        try:
            cid = self.get_argument('cid')
        except Exception as e:
            logging.error(e)
            retData = self._returnData(False,'error_parameter')
        else:
            commodityData = self.db.query_one(table='tab_com_infos',whereFieldValue=" ci_id = '" + cid + "'")
            print(commodityData)
            if commodityData:
                data = {
                    'id':commodityData[0]['ci_id'],
                    'title':commodityData[0]['ci_title'],
                    'infos':commodityData[0]['ci_infos'],
                    'ordprice':self._getMoney(commodityData[0]['ci_oprice']),
                    'newprice':self._getMoney(commodityData[0]['ci_nprice']),
                    'sales':commodityData[0]['ci_sales'],
                    'class':[commodityData[0]['ci_class'],self._getClass(commodityData[0]['ci_class'])],
                    'img':config.cPicPath + commodityData[0]['ci_img'],
                    'freight':self._getMoney(commodityData[0]['ci_freight']),
                    'specifications':commodityData[0]['ci_specifications'],
                    'excellent':commodityData[0]['ci_excellent'],
                    'hot':commodityData[0]['ci_hot']
                }
                retData = self._returnData(True,data)
            else:
                retData = self._returnData(False,'error_db')
        self.write(retData)