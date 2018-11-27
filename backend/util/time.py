import time

class GetTime(object):
    def __init__(self):
        self.format_timestamp = time.localtime(int(time.time()))
        self.time_now = time.strftime("%Y%m%d%U%w%H%M%S", self.format_timestamp)

    def gettime(self,need_time_str = '年月日 星期'):
        """
        作用：获取带中文格式化后的时间
        传入参数：需要获取的数据的单词首字母,例('年月日'),中间出现未定义字符(例如空格或标点符号)时
                                ,  将该字符加入其中后返回
        返回：带中文后的日期或时间,例：gettime('年月日 星期')    return '2018年10月15日 星期一'
        """
        # need_time_str = need_time_str.lower()
        retTime = ''
        for x in need_time_str:
            if x in '年月日周星时分秒&':
                if x == '年':
                    retTime += str(self.time_now[:4]) + '年'
                if x == '月':
                    retTime += str(self.time_now[4:6]) + '月'
                if x == '日':
                    retTime += str(self.time_now[6:8]) + '日'
                if x == '周':
                    retTime += str(self.time_now[8:10]) + '周'
                if x == '星':
                    retTime += '星期' + str(self.__getweek(self.time_now[10:11]))
                if x == '时':
                    retTime += str(self.time_now[11:13]) + '时'
                if x == '分':
                    retTime += str(self.time_now[13:15]) + '分'
                if x == '秒':
                    retTime += str(self.time_now[15:17]) + '秒'
                if x == '&':
                    retTime += '&nbsp;&nbsp;&nbsp;&nbsp;'
            else:
                retTime += x

        return retTime

    def __getweek(self,weekNum):
        if weekNum == '0':
            return '天'
        if weekNum == '1':
            return '一'
        if weekNum == '2':
            return '二'
        if weekNum == '3':
            return '三'
        if weekNum == '4':
            return '四'
        if weekNum == '5':
            return '五'
        if weekNum == '6':
            return '六'