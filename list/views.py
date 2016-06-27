from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item,List
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
    list_ = List.objects.create()
    Item.objects.create(text=request.POST.get('item_text',''),list=list_)
    return redirect('/list/the-only-list-in-the-world/')
