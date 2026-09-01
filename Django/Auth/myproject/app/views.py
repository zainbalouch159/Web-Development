from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(req):
    if req.method=="POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return render(req,"dashboard.html")
        else:
            return render("register", {"form":form})