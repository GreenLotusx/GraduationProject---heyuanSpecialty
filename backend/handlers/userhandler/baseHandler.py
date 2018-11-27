from handlers.baseHandler import BaseHandler

class BaseHandler(BaseHandler):
    def _getSex(self,num):
        num = str(num)
        if num == '1':
            return 'male'
        elif num == '2':
            return 'female'
        elif num == 'male':
            return '1'
        elif num == 'female':
            return '2'

    def _formatAddress(self,address):
        """格式化address中的空格为前端html显示的空格转义字符"""
        if address != None:
            address = address.replace(' ','&nbsp;')
        else:
            address = '用户没有默认收货地址'
        return address