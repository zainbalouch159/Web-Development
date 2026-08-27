from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def indexview(req,):
    return render(req,"index.html")

def aboutview(req):
    return render(req,"about.html")

def detail_save(req):
    print(req.POST)
    return HttpResponse("Detail saved")

