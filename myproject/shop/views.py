
from .models import Item
# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, resolve_url, render
def view1(request): return HttpResponseRedirect('/shop/')
def view2(request):
    url = resolve_url('shop:item_list')
    return HttpResponseRedirect(url)
def view3(request):
    return redirect('shop:item_list')

def test_view(request):
    return HttpResponse(status=201)



def item_list(request):
    qs=Item.objects.all()
    return render(request,'shop/Item_list.html',{
        'item_list':qs,
    })

def archives_year(request,year):
    return HttpResponse('{}년도에 대한 내용'.format(year))