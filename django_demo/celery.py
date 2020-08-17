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


os.environ.setdefault("DJANGO_SETTINGS_MODULE","dj3_demo.settings")

app = Celery("dj3_demo")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)