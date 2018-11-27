from app import config
from handlers.commodityHandler.baseHandler import BaseHandler

class RecommendCommoditiesHandler(BaseHandler):
    def get(self):
        """获取最多五个优质商品和有且只有两个热卖商品"""
        excellentData = self.db.query_many(num=5,whereFieldValue="where ci_excellent = " + str(1))
        hotData = self.db.query_many(num=2,whereFieldValue="where ci_hot = " + str(1))
        excellent = []
        hot = []
        if excellentData:
            for item in excellentData:
                idata = {
                    'id': item['ci_id'],
                    'img': config.cPicPath + item['ci_img']
                }
                excellent.append(idata)
        if hotData:
            for item in hotData:
                idata = {
                    'id': item['ci_id'],
                    'img': config.cPicPath + item['ci_img']
                }
                hot.append(idata)
        data = {
            'hot':hot,
            'excellent':excellent
        }
        if len(hot) != 0 and len(excellent) != 0:
            retData = self._returnData(True,data)
        else:
            retData = self._returnData(False,'error_db')
        self.write(retData)