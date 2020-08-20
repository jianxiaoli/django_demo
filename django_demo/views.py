from django.shortcuts import render, redirect


def index(request):
    # 获取当前用户的随机字符串
    # 根据随机字符串获取对应信息
    if request.COOKIES.get('is_login'):
        return render(request, 'index.html')
    else:
        return redirect('/user/to_login')