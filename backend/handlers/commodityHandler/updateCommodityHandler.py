from util.loginDecorator import decorator
from util.commodityPic import CommodityPic
from handlers.commodityHandler.baseHandler import BaseHandler

class UpdateCommodityHandler(BaseHandler):
    @decorator
    def post(self):
        if self.session.data.get('identity') <= 1:
            cid = self.get_argument('cid')
            parameter = eval(self.get_argument('fromParameter'))
            file = self.request.files.get('file')
            wfv = " ci_id = '" + cid + "'"
            title = " ci_title = '" +  parameter['title']
            infos = "', ci_infos = '" + parameter['infos']
            ordPrice = "', ci_oprice = '" +self._formatMoney(parameter['ordprice'])
            newPrice = "', ci_nprice = '" +self._formatMoney(parameter['newprice'])
            freight = "', ci_freight = '" + self._formatMoney(parameter['freight'])
            picClass = "', ci_class = '" + parameter['picClass']
            specifications = "', ci_specifications = '" + parameter['specifications']
            sfv = title + infos + ordPrice + newPrice + freight + picClass + specifications +"'"
            if parameter['hot'] != 'None':
                hot = ", ci_hot = '" + parameter['hot'] + "'"
                sfv += hot
            if parameter['excellent'] != 'None':
                excellent = ", ci_excellent = '" + parameter['excellent'] + "'"
                sfv += excellent

            if file:
                commodityPic = CommodityPic(file)
                path = commodityPic.writeFile()
                if path:
                    path = ", ci_img = '" + path +"'"
                    sfv = sfv + path
                else:                                                                                               #这里path没有返回值，说明文件操作出现异常
                    return self.write(retData = self._returnData(False,'error_file'))
            print(wfv)
            print(sfv)
            result = self.db.update(whereFieldValue=wfv, setFieldValue=sfv, table='tab_com_infos')
            if result:
                retData = self._returnData(True,'商品信息修改成功')
            else:
                retData = self._returnData(False,'error_db')
        else:
            retData = self._returnData(False,'error_identity')
        self.write(retData)