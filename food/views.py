from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms  import Itemform
from django.views.generic import CreateView,DetailView

from django.urls import reverse_lazy
# Create your views here.


def index(request):
    item_list=Item.objects.all()
    context={
        "item_list":item_list,
    }
    return render(request,"food\index.html",context)

class details(DetailView):
    model=Item
    template_name="food\details.html"


class create_item(CreateView):
    model = Item
    fields = [ 'item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item_form.html'

    def form_valid(self, form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)
   


def update_item(request,id):
    item=Item.objects.get(pk=id)
    form=Itemform(request.POST or None,instance=item)
    if form.is_valid():
        form.save()
        return redirect(to='food:index')
    return render(request,'food/item_form.html',{'form':form,'item':item})


def delete_item(request,id):
    item=Item.objects.get(pk=id)
    if request.method== 'POST':
        item.delete()
        return redirect(to='food:index')
    return render(request,'food/item_delete.html',{'item':item})