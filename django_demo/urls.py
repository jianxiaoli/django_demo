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
from django.urls import path

import django_demo
import user
from django_demo import views
from user import views

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^$', django_demo.views.index),
    url(r'^index', django_demo.views.index, name='index'),

    # user urls
    url(r'^user/to_login', user.views.to_login, name='to_login'),
    url(r'^user/to_register', user.views.to_register, name='to_register'),
    url(r'^user/register', user.views.register, name='register'),
    url(r'^user/login', user.views.login, name='login'),
    path('user/active/<token>', user.views.active),
]

handler400 = django_demo.views.bad_request
handler403 = django_demo.views.permission_denied
handler404 = django_demo.views.page_not_found
handler500 = django_demo.views.server_error