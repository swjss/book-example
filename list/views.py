from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
# Create your views here.
'''
home_page 是首页的调用函数
'''
def home_page(request):
#    return HttpResponse(b"<html><title>To-Do lists</title></html>")
#    if request.method == 'POST':
#        return HttpResponse(request.POST['item_text'])
    if request.method == 'POST':
        item=Item()
        item.text=request.POST.get('item_text','')
        item.save()
        return redirect('/list/the-only-list-in-the-world')
    return render(request,'home.html')

def view_list(request):
    items=Item.objects.all()
    return render(request,'list.html',{'items':items})
