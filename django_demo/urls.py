"""django_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin

import django_demo
from django_demo import views
from django_demo.apps.user import views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$', django_demo.views.index),
    url(r'^index', django_demo.views.index, name='index'),
    url(r'^user/to_login', django_demo.apps.user.views.to_login, name='to_login'),
    url(r'^user/to_register', django_demo.apps.user.views.to_register, name='to_register'),
    url(r'^user/register', django_demo.apps.user.views.register, name='register'),
    url(r'^user/login', django_demo.apps.user.views.login, name='login'),
    ]