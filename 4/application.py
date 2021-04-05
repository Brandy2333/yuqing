# 词云系统
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os
from common.libs.UrlManager import UrlManager

class Application(Flask):
    def __init__(self,import_name,template_folder=None,root_path=None):
        super(Application,self).__init__(import_name,template_folder=template_folder,static_folder=None,root_path=root_path)
        self.config.from_pyfile('config/local_setting.py') #加载本地配置文件

        # todo:按环境加载配置文件

        db.__init__(self)

db = SQLAlchemy() #链接数据库的方式
app = Application(__name__,template_folder=os.getcwd()+'/web/templates',root_path=os.getcwd()) #配置文件，网页的模板地址在哪个目录下
#后面的为根目录
manager = Manager(app) # 运行app

# 函数模板,使得在html中也可以调用python方法
app.add_template_global(UrlManager.buildStaticUrl,"buildStaticUrl") #指定静态地址的方法
app.add_template_global(UrlManager.buildUrl,"buildUrl") # 指定地址




