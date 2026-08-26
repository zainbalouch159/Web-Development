from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def indexview(req,):
    return render(req,"index.html")
def aboutview(req):
    return render(render,"about.html")

