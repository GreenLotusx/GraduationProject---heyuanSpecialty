from handlers.baseHandler import BaseHandler

class BaseHandler(BaseHandler):
    def _getMoney(self,mNum):
        """传入以分为单位的金额数,计算出以元为单位的金额并返回"""
        if mNum != 0:
            mNum = int(mNum)
            money = format(float(mNum) / float(100), '.2f')
        else:
            money = '0.00'
        return money