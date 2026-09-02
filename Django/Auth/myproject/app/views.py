from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(req):
    if req.method=="POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
        else:
            return render(req,"register.html", {"form":form})
    else:
        return render(req,"register.html")
    
def Login(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("password")
        if not username and not password:
            return redirect("login")
        else:
            user = authenticate(request=req,username=username,password=password)
            if user is not None:
                login(req,user)
                return redirect("dashboard")
            else:
                error= "Invalid password or username "
                return render(req,"login.html",{"error":error})
    return render(req,"login.html")
def dashboard(req):
    return render(req,"dashboard.html")