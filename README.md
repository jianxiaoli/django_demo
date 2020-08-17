python 3.6.4
celery需要分端口


dop_comm   为公共库

asset  资产管理，celery端口6373

web  服务树，celery端口6376

admin_web  后端程序，celery端口6378


VirutalEnv
pip install virtualenv
添加环境变量
mkdir /opt/venv
/usr/local/python3/bin/virtualenv -p /usr/bin/python3 /opt/venv/phenas


生成requirements.txt
1、生成架包依赖文件
(venv) D:\code\flask_demo>pip freeze > requirements.txt
2、安装依赖架包
(venv) D:\code\flask_demo>pip install -r requirements.txt

windows下需要安装pypiwin32才能支持多进程写日志
pip install pypiwin32

6、alembic基本使用
https://www.cnblogs.com/xiaoming279/p/6641601.html
python run.py db migrate
python run.py db upgrade
python run.py db downgrade