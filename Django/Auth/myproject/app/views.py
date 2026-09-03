from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .middlewares import auth,guest
# Create your views here.

@guest
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

@guest    
def Login(req):
    if req.method == 'POST':
        username = req.POST.get("username")
        password = req.POST.get("password")
        if not username and not password:
            return redirect("/")
        else:
            user = authenticate(request=req,username=username,password=password)
            if user is not None:
                login(req,user)
                return redirect("dashboard")
            else:
                error= "Invalid password or username "
                return render(req,"login.html",{"error":error})
    return render(req,"login.html")

def user_Logout(req):
    logout(req)
    return redirect("/")

@auth
def dashboard(req):
    user = req.user
    return render(req,"dashboard.html",{"user":user})