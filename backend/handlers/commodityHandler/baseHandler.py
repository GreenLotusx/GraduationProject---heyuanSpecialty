from decimal import Decimal
from handlers.baseHandler import BaseHandler

class BaseHandler(BaseHandler):
    def _getClass(self,clsNum):
        clsNum = str(clsNum)
        if clsNum == '1':
            return '零食类特产',
        elif clsNum == '2':
            return '水果类特产'
        elif clsNum == '3':
            return '小吃类特产'
        elif clsNum == '4':
            return '手工类特产'
        elif clsNum == '5':
            return '其他类特产'
        elif clsNum == '零食类特产':
            return '1'
        elif clsNum == '水果类特产':
            return '2'
        elif clsNum == '小吃类特产':
            return '3'
        elif clsNum == '手工类特产':
            return '4'
        elif clsNum == '其他类特产':
            return '5'

    def _getMoney(self,mNum):
        """传入以分为单位的金额数,计算出以元为单位的金额并返回"""
        if mNum != 0:
            mNum = int(mNum)
            money = format(float(mNum) / float(100), '.2f')
        else:
            money = '0.00'
        return money

    def _formatMoney(self,mNum):
        """
            格式化传入以元为单位的金额数字，将其转化成分，以便插入数据库
            这里使用了Decimal来解决浮点精度问题，开发过程中不做处理时，返回数值计算不准确
        """
        mNum = Decimal(str(mNum))
        mNum = int(mNum * Decimal('100'))
        print('传出：',end='')
        print(mNum)
        return str(mNum)