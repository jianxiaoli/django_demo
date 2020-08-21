python 3.6.4
celery需要分端口



VirutalEnv
pip install virtualenv
添加环境变量
mkdir /opt/venv
/usr/local/python3/bin/virtualenv -p /usr/bin/python3 /opt/venv/django_demo


生成requirements.txt
1、生成架包依赖文件
pip freeze > requirements.txt
2、安装依赖架包
pip install -r requirements.txt

写日志windows下需要安装pypiwin32才能支持多进程写日志
pip install pypiwin32

需要指定环境变量
export DJANGO_ENV=dev

本地运行
python manage.py  runserver