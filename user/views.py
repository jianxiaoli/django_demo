from django.http import HttpResponse
from django.shortcuts import render

def toLogin(request):
    return render(request, 'login.html')

def toRegister(request):
    return render(request, 'register.html')