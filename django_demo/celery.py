# -*- coding: UTF-8 -*

# 标准库
from __future__ import unicode_literals, absolute_import
import os
# 第三方库
from celery import Celery
from django.conf import settings
# 自定义库

__version__ = ''
__all__ = []


os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_demo.settings") #设置django环境

app = Celery("django_demo")
app.config_from_object("django.conf:settings") #使用CELERY_ 作为前缀，在settings中写配置
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)