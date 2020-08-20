import re

from django.contrib.auth.hashers import make_password, check_password
from django.core import serializers
from django.http import HttpResponse, response, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from pip._vendor.requests import Response

from django_demo.apps.user.models import UserInfo
from django_demo.utils.response_helper import MyResponse, ResState


def to_login(request):
    return render(request, 'login.html')

def to_register(request):
    return render(request, 'register.html')

@require_http_methods(["POST"])
def register(request):
    myRes = MyResponse()
    username = request.POST.get("username")
    email = request.POST.get("email")
    pwd = request.POST.get("pwd")
    pwd_ok = request.POST.get("pwd_ok")
    try:
        if not re.match(r"^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", email):
            # 返回错误信息
            return myRes.to_json_msg("邮箱格式不正确")
        elif pwd != pwd_ok:
            return myRes.to_json_msg("密码不一致，请重新输入")
        user = UserInfo.objects.filter(username=username)
        if user:
            return myRes.to_json_msg("用户名已存在")
        pwd = make_password(pwd, None, 'pbkdf2_sha256')
        obj = UserInfo(username=username, pwd=pwd,email=email)
        obj.save()
        myRes.status = ResState.HTTP_SUCCESS
    except Exception as ex:
        print(ex)
        myRes.msg = str(ex)

    return myRes.to_json()

@require_http_methods(["POST"])
def login(request):
    myRes = MyResponse()
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    try:
        try:
            user = UserInfo.objects.get(username=username)
        except Exception as ex:
            print(ex)
            return myRes.to_json_msg("用户不存在")
        pwd_bool = check_password(pwd, user.pwd)
        if not pwd_bool:
            return myRes.to_json_msg("密码错误")
        myRes.status = ResState.HTTP_SUCCESS
        myRes.msg = "登录成功"
        return myRes.to_login_json("1")
    except Exception as ex:
        print(ex)
        myRes.msg = str(ex)
        return myRes.to_json()