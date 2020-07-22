from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# Create your views here.

def item_list(request):
    qs=Item.objects.all()
    return render(request,'shop/Item_list.html',{
        'item_list':qs,
    })

def archives_year(request,year):
    return HttpResponse('{}년도에 대한 내용'.format(year))