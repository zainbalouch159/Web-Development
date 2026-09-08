from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_view(req):
    if req.method=='POST':
        username = req.POST.get('Username')
        password = req.POST.get('password')
        user = authenticate(req,username=username,password=password)
        if user is not None:
            login(req,user)
            return redirect('home')
        else:
            return render(req,'login.html',{'error':'Username or password is not correct'})
    else:
        return render(req,'login.html')
    
def register(req):
    if req.method=='POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(req,'register.html',{'form':form})
    else:
            return render(req,'register.html')
        