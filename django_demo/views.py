from django.shortcuts import render, redirect

from django_demo import logger


def index(request):
    return render(request, 'index.html')
    # if request.COOKIES.get('is_login'):
    #     return render(request, 'index.html')
    # else:
    #     return redirect('/user/to_login')