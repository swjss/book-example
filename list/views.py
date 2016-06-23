from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
home_page 是首页的调用函数
'''
def home_page(request):
#    return HttpResponse(b"<html><title>To-Do lists</title></html>")
    return render(request,'home.html')
