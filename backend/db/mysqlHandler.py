import pymysql
import inspect
from util.constants import PAGE_NUM
from app.config import mysql_config

class DBHandler(object):
    """
    数据库类的操作，
    """

    def __init__(self):
        self.db = pymysql.connect(**mysql_config)  #tab_pic_data
        self.cursor = self.db.cursor()

    def add(self,table,**kwargs):
        """增加一条数据"""
        sql = ("insert into " + table + str(tuple(kwargs.keys())).replace("'","")
               + " values "
               + str(tuple(kwargs.values()))
               + ";"
               )
        return self.__execute(sql, table,operation=inspect.stack()[0][3])


    def delete(self,whereFieldValue,table):
        """删除一条数据"""
        sql = ("delete from " + table
               + " where " + whereFieldValue
               + ";"
               )
        return self.__execute(sql, table,operation=inspect.stack()[0][3])

    def update(self,whereFieldValue,setFieldValue,table):
        """更新一条数据setFieldValue值为一个字符串,里面为要更新的字段以及值,例（id=‘12’）"""
        sql = (
                "update " + table
                + " set " + setFieldValue
                + " where "+ whereFieldValue
                +";"
        )
        return self.__execute(sql, table,operation=inspect.stack()[0][3])

    def query_oderyBy(self,whereFieldValue,sortField,num,table,sortMode='desc'):
        """通过一个字段查询另外某一字段排序后的n条数据"""
        sql = (
            "select *"
            + " from "+table
            + " where "+whereFieldValue
            + " order by " + sortField +" "
            + sortMode
            + " limit " + str(num)
            +";"
        )
        return self.__execute(sql, table, operation=inspect.stack()[0][3])

    def query_one(self,whereFieldValue,table):
        """查询一条数据，必需参数：字符串(查询字段 = 查询字段的值)"""
        sql = ("select *"
                    + " from "+table
                    + " where " + whereFieldValue
                    + ";"
               )
        return self.__execute(sql, table,operation=inspect.stack()[0][3])                  ##将方法名传入作参数

    def query_many(self,num=PAGE_NUM,whereFieldValue='',sortField='ci_id',table='tab_com_infos',sortMode='desc'):
        """查询数据库最新n条数据，默认whereFieldValue值为空,当要传入值时,必须在传入值前面加上where关键字"""
        sql = ("select *"
               + " from " + table + " "
               +  whereFieldValue
               + " order by " + sortField + " "
               + sortMode
               + " limit " + str(num)
               +";"
               )
        return self.__execute(sql, table,operation=inspect.stack()[0][3])

    def query_like(self,likeField,likeValue,table,num=PAGE_NUM):
        """查询数据库中某字段包含某字符的数据"""
        sql = ("select *"
               + " from " + table
               + " where " + likeField
               + " like " + "'%" + str(likeValue) +"%'"
                +" limit " + str(num)
               +";"
               )
        return self.__execute(sql,table,operation=inspect.stack()[0][3])

    def  query_sum(self,table='tab_com_infos'):
        """查询一共有多少条数据"""
        sql = (
            "select count(1) from " + table
            +";"
        )
        return self.__execute(sql, table,operation=inspect.stack()[0][3])


    def query_custom(self,sql):
        """自定义查询语句,具体sql语句由外部调用时直接输入"""
        return self.__execute(sql, operation=inspect.stack()[0][3])

    def __execute(self,sql,table='tab_pic_data',operation='query_one'):
        """提交sql语句，执行"""
        result = True
        try:
            num = self.cursor.execute(sql)
            if num == 0:
                return num
            else:
                    result = self.cursor.fetchall()
            self.db.commit()
        except Exception as e:
            print(e)
            result = False
            self.db.rollback()
        if not result:
            if isinstance(result,tuple) and 'query' not in operation:
                result = True
        return result


    def close(self):
        # 关闭数据库连接
        print("----------------------数据库链接关闭-----------------------")
        self.db.close()

    def __del__(self):
        self.close()
