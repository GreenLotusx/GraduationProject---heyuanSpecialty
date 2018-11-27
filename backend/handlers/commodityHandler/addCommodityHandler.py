import logging
from util.commodityPic import CommodityPic
from handlers.commodityHandler.baseHandler import BaseHandler

class AddCommodityHandler(BaseHandler):
    def post(self):
        if self.session.data.get('identity') <= 1:
            parameter = self.get_argument('fromParameter')
            parameter = eval(parameter)
            file = self.request.files.get('file')
            if file:
                commodityPic = CommodityPic(file)
                path = commodityPic.writeFile()
                list = {
                    'ci_title': parameter['title'],
                    'ci_infos': parameter['infos'],
                    'ci_oprice': self._formatMoney(parameter['ordprice']),
                    'ci_nprice': self._formatMoney(parameter['newprice']),
                    'ci_freight': self._formatMoney(parameter['freight']),
                    'ci_class': parameter['picClass'],
                    'ci_img': path,
                    'ci_specifications': parameter['specifications'],
                    'ci_excellent': parameter['excellent'],
                    'ci_hot': parameter['hot']
                }
                result = self.db.add(table='tab_com_infos', **list)
                if result:
                    retData = self._returnData(True, '商品添加成功')
                else:
                    retData = self._returnData(False, 'error_db')
            else:
                retData = self._returnData(False, 'error_need')
        else:
            self._returnData(False,'error_identity')
        self.write(retData)