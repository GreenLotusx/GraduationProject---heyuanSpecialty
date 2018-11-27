import functools

def decorator(fun):
	@functools.wraps(fun)					#保证被装饰的函数对象__name__不变
	def wrapper(obj,*args,**kwargs):
		if not obj.get_current_user():
			print('没有登陆')
			retData = obj._returnData(False,'error_notlogin')
			obj.write(retData)
		else:
			fun(obj,*args,**kwargs)
	return wrapper