import time
import logging
from app.config import cPicPath

class CommodityPic(object):
    def __init__(self,fileData):
        self.__fileData = fileData

    def writeFile(self):
        fName = str(int(time.time()))  ##将时间戳作为文件名称
        print(fName)
        try:
            file = open(cPicPath + fName+'.jpg','wb')
            file.write(self.__fileData[0].get('body'))
            file.close()
        except Exception as e:
            logging.error(e)
        else:
            return fName+'.jpg'