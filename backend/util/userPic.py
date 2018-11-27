import time
import logging
from app.config import uPicPath,usePicSize
from PIL import Image

class UserPic(object):
    def __init__(self,fileData):
        self.__fileData = fileData

    def __writeFile(self):
        fName = str(int(time.time()))  ##将时间戳作为临时文件名称
        try:
            file = open(uPicPath + fName+'.png','wb')
            file.write(self.__fileData[0].get('body'))
            file.close()
        except Exception as e:
            print('发生错误')
            logging.error(e)
        else:
            return fName+'.png'

    def __changeSize(self,ordName):
        fName = str(int(time.time()))  ##将时间戳作为新文件名称
        im = Image.open(uPicPath + ordName)
        out = im.resize(usePicSize, Image.ANTIALIAS)
        out.save(uPicPath + fName + '.png')
        return fName + '.png'

    def getUsePic(self):
        picPath = self.__writeFile();
        path = self.__changeSize(picPath)
        return path