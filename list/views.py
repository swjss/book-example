from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
# Create your views here.
'''
home_page 是首页的调用函数
'''
def home_page(request):
    return render(request,'home.html')

def view_list(request):
    items=Item.objects.all()
    return render(request,'list.html',{'items':items})
def new_list(request):
    Item.objects.create(text=request.POST.get('item_text',''))
    return redirect('/list/the-only-list-in-the-world/')
