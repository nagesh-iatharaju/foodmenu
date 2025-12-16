from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Item
from .forms  import Itemform
# Create your views here.


def index(request):
    item_list=Item.objects.all()
    context={
        "item_list":item_list,
    }
    return render(request,"food\index.html",context)

def details(request,item_id):
    item=Item.objects.get(pk=item_id)
    context={
        "item":item,
    }
    return render(request,"food\details.html",context)

def create_item(request):
    form=Itemform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(to="food:index")
    return render(request,"food\item_form.html",{"form":form})