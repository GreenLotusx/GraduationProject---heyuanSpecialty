# Graduation Design - Heyuan Special Products

## Simple Description
	This is a graduation project. It is a simple e-commerce website. 
	It realizes the basic functions of registration,login, commodity purchase,
	order processing, analog payment, shopping cart and background to add or delete or modify commodity information.
	Its back end is provided by Tornado, Python's web framework.
	
## Environmental Dependence
	Python3.x (Python 3.6.4)
	Tornado   (Tornado 5.1.1)
	MySQL	  (Mysql 8.0.13)
	PyMySQL   (PyMySQL 0.9.2)
	Pillow    (Pillow 5.3.0)
	redis     (redis 2.10.6)
	
	Among them, except for Python 3, there is no mandatory dependency on the version.
	Dependent libraries can be installed directly through pip, such as pip3 install Tornado.
	
## Instructions
+ Before use, the environment must depend on correct installation and configuration. See the above steps for specific installation.

+ Before running the project, we must use MySQL client to build database, tables and so on. Specific SQL statements are under **project/backend/db/db.sql**. You can use the command **source project/backend/db/db.sql** on the MySQL client; you can perform database building and table building operations. 

+ Change part of the configuration, which is modified according to your own needs. The configuration file is located in **project/backend/app/config.py**.

+ Before running, make sure that port **8000** is not occupied.

+ Under project/backend/folder, the terminal executes **python 3 server.py-port=8000**.

+ open http://localhost:8000 in your browser.

+ If you can successfully open the page, you can login through the default account root, administrator users will jump directly to the background management interface, and then you can operate the commodity data.

*The above project folder is your project folder*.  
*The default password for root account is **123456***.

## Effect Picture
![](https://github.com/GreenLotusx/GraduationProject---heyuanSpecialty/blob/master/frontend/static/images/projectImg/2018-11-27%2012-55-48%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)  

![](https://github.com/GreenLotusx/GraduationProject---heyuanSpecialty/blob/master/frontend/static/images/projectImg/2018-11-27%2012-57-43%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)  

![](https://github.com/GreenLotusx/GraduationProject---heyuanSpecialty/blob/master/frontend/static/images/projectImg/2018-11-27%2012-56-16%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)  

![](https://github.com/GreenLotusx/GraduationProject---heyuanSpecialty/blob/master/frontend/static/images/projectImg/2018-11-27%2012-56-40%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)  

![](https://github.com/GreenLotusx/GraduationProject---heyuanSpecialty/blob/master/frontend/static/images/projectImg/2018-11-27%2012-56-59%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)  

![](https://github.com/GreenLotusx/GraduationProject---heyuanSpecialty/blob/master/frontend/static/images/projectImg/2018-11-27%2012-57-16%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE.png)



