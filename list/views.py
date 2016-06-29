from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item,List
# Create your views here.
'''
home_page 是首页的调用函数
'''
def home_page(request):
    return render(request,'home.html')

def view_list(request,list_id):
    list_ = List.objects.get(id=list_id)
    items = Item.objects.filter(list = list_)
    return render(request,'list.html',{'items':items,'list':list_})
def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST.get('item_text',''),list=list_)
    return redirect('/list/%d/' % (list_.id,))

def add_item(request,list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST.get('item_text',''),list=list_)
    return redirect('/list/%d/'%(list_.id,))
