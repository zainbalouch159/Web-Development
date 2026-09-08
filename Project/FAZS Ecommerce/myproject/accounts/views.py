from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def login(req):
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