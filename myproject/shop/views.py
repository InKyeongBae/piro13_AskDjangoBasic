import logging
import re
from .models import Item
# Create your views here.
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import redirect, resolve_url, render, get_object_or_404
from .forms import ItemForm
from django.views.generic import CreateView, UpdateView


def view1(request): return HttpResponseRedirect('/shop/')
def view2(request):
    url = resolve_url('shop:item_list')
    return HttpResponseRedirect(url)
def view3(request):
    return redirect('shop:item_list')

def test_view(request):
    return HttpResponse(status=201)
logger = logging.getLogger(__name__)


def item_list(request):
    qs = Item.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(name__icontains=q)

    logger.debug('query : {}'.format(q))

    return render(request, 'shop/item_list.html', {
        'item_list': qs,
        'q':q,
    })

def archives_year(request,year):
    return HttpResponse('{}년도에 대한 내용'.format(year))

def item_detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    return render(request,'shop/item_detail.html',{
        'item':item,


    })

# def item_new(request, item=None):
#     if request.method=='POST':
#         form=ItemForm(request.POST,request.FILES,instance=item)
#         if form.is_valid():
#             item=form.save()
#             return redirect(item)
#     else:
#         form=ItemForm(instance=item)
#     return render(request,'shop/item_form.html',{
#         'form':form,
#     })

# def item_edit(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     return item_new(request, item)

item_new=CreateView.as_view(model=Item,form_class=ItemForm)

item_edit=UpdateView.as_view(model=Item,form_class=ItemForm)