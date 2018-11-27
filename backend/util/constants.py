ERROR_CODE = {                                  ##状态码
    'success':0,                                        #成功
    'error':-1,                                           #一般异常,
    'error_notlogin':-2,                           #没有登陆
    'error_identity':-10,                           ##没有权限
    'error_logout':-5,                               #登出异常
    'error_userinfos':-10,                        #获取用户信息异常
    'error_ordpwd':-20,                          #旧密码不正确
    'error_changePwd':-21,                     #密码更改异常(旧密码正确,数据库更新发生异常)
    'error_noChanged': -22,                     # 新旧密码一样
    'error_useExist':-30,                           #用户已存在
    'error_mailboxExist':-31,                    #邮箱已被注册
    'error_failed':-32,                                #注册失败
    'error_query':-50,                                 #查询数据异常
    'error_need':-60,                               #缺少传入异常
    'error_file':-70,                                   #文件操作异常
    'error_noRecord':-81,                        #没有指定数据
    'error_db':-500,                                #数据库异常
    'error_login':-200,                           #登陆异常
    'error_parameter':-108,                  #参数异常
    'error_server':500,                           #服务器异常
}


ERROR_MSG = {                       ##响应消息
    'success':'success',
    'error':'commonly error',
    'error_notlogin':'no login account',
    'error_logout':'logout exception',
    'error_identity':'users do not have permission',
    'error_userinfos':'get abnormal user information',
    'error_db':'exception occurred during database operation',
    'error_login':'abnormality of landing',
    'error_noRecord':'no relevant records were found',
    'error_ordpwd':'old password is incorrect',
    'error_changePwd':'password update failed',
    'error_noChanged':'the password has not changed',
    'error_useExist':'user already exists',
    'error_need':'also need to import image files',
    'error_query':'an exception occurred in the query operation',
    'error_mailboxExist':'the mailbox has been registered',
    'error_failed':'user creation failure',
    'error_file':'there was an exception in file read and write',
    'error_parameter':'abnormal upload parameters',
    'error_server':'server exception'
}

PAGE_NUM = 20                       ##每页显示数据的数量

                                                    #操作数据库关键字，提交内容包含该字段则替换掉
DB_KEYS = ['where','update','delete','query','order','desc','limit','from','select']

REDIS_INDEX_KEY_NAME = 'db_index'
REDID_INDEX_SLIDES_KEY_NAME = 'db_index_slides'