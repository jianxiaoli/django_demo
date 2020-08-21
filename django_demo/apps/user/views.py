import re

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from django_demo.apps.user.models import UserInfo
from django_demo.utils.response_helper import MyResponse, ResState


### 跳转到登录页面
from django_demo.utils.token_handler import TokenHandler


def to_login(request):
    return render(request, 'login.html')

### 跳转到注册页面
def to_register(request):
    return render(request, 'register.html')

### 注册
@require_http_methods(["POST"])
def register(request):
    myRes = MyResponse()
    username = request.POST.get("username")
    email = request.POST.get("email")
    pwd = request.POST.get("pwd")
    pwd_ok = request.POST.get("pwd_ok")
    try:
        if len(username) < 6 or len(username) > 64:
            return myRes.to_json_msg("用户名长度应在6-64之间")
        if not re.match(r"^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$", email):
            # 返回错误信息
            return myRes.to_json_msg("邮箱格式不正确")
        elif pwd != pwd_ok:
            return myRes.to_json_msg("密码不一致，请重新输入")
        user = UserInfo.objects.filter(username=username).first()
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

### 登录
@require_http_methods(["POST"])
def login(request):
    myRes = MyResponse()
    username = request.POST.get("username")
    pwd = request.POST.get("pwd")
    try:
        user = UserInfo.objects.filter(username=username).first()
        if user is None:
            raise Exception("用户不存在")
        if user.is_enabled == 1:
            return myRes.to_json_msg("请先激活账号")
        pwd_bool = check_password(pwd, user.pwd)
        if not pwd_bool:
            return myRes.to_json_msg("密码错误")
        myRes.status = ResState.HTTP_SUCCESS
        myRes.msg = "登录成功"
        token = TokenHandler().build_token(user.id)
        return myRes.to_login_json(token)
    except Exception as ex:
        print(ex)
        myRes.msg = str(ex)
        return myRes.to_json()