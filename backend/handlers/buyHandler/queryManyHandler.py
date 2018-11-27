from app import config
from util.loginDecorator import decorator
from handlers.buyHandler.baseHandler import BaseHandler

class QueryManyHandler(BaseHandler):
    @decorator
    def post(self, *args, **kwargs):
        print(self.json_args)
        cidList = self.json_args.get('cidList')
        print('传入参数：')
        print(cidList)
        if cidList:
            comList = []
            for item in cidList:
                print(item)
                commodityData = self.db.query_one(table='tab_com_infos', whereFieldValue=" ci_id = '" + item[0] + "'")
                if commodityData:
                    data = {
                        'id': commodityData[0]['ci_id'],
                        'title': commodityData[0]['ci_title'],
                        'price': self._getMoney(commodityData[0]['ci_nprice']),
                        'img': config.cPicPath + commodityData[0]['ci_img'],
                        'freight': self._getMoney(commodityData[0]['ci_freight']),
                        'specifications': commodityData[0]['ci_specifications'],
                        'num':item[1],
                        'sprice':self._getMoney(int(item[1]) * int(commodityData[0]['ci_nprice']) + commodityData[0]['ci_freight'])
                    }
                    comList.append(data)
                else:
                    retData = self._returnData(False,'error_db')
            if comList:
                retData = self._returnData(True,comList)
            else:
                retData = self._returnData(False,'erro_db')
        else:
            retData = self._returnData(False,'error_login')
        self.write(retData)