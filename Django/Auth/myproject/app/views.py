from django.shortcuts import render,redirect

# Create your views here.

def app(req):
    return render(req,"register.html")