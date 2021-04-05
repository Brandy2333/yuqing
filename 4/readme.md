# 系统运行方法  

进入4目录，终端输入：cd 4  
终端输入：python manager.py run  
所需库文件请查阅requirments.txt  
即可在[127.0.0.1:5000]访问该系统  
[127.0.0.1:5000/wordcloud/]为本次作业内容  

## 目录结构  

本系统采用MVC框架  
  
···  
  
···  
  
########################################  
service firewalld stop--关闭防火墙  

## 报错解决  

vscode中/web/controllers/static.py报错  
修改.vscode文件为  
···  
{  
    "python.pythonPath": "/home/apr/anaconda3/envs/api_misuse/bin/python",  
    // "terminal.integrated.env.osx": {"PYTHONPATH": "${workspaceFolder}"},  
    "python.linting.pylintArgs": [  
        // "--disable=F0401"  
        "--disable=E0401"  
    ]  
}  
···  
  
## flask-sqlacodegen  
  
    flask-sqlacodegen 'mysql+pymysql://name:password@127.0.0.1/table' --outfile "common/models/model.py"  
    flask-sqlacodegen 'mysql+pymysql://root:123456@127.0.0.1/table' --tables user --outfile "common/models/user.py"   
    flask-sqlacodegen 'mysql+pymysql://root:123456@127.0.0.1/cucnews' --tables news2 --outfile "common/models/model.py" --flask 
##########################################  
