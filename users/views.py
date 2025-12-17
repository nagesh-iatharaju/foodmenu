from django.shortcuts import render,redirect
from .forms import Registerform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request,):
    if request.method=="POST":
        form=Registerform(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request,f'welcome {username},your account is created')
            form.save()
            return redirect(to='login')
    else:
        form=Registerform()
    return render(request,"users/register.html",{'form':form}) 

@login_required
def profilepage(request):
    return render(request,'users/profile.html')