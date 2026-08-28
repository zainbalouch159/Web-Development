from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Note

# Create your views here.


def indexview(req):
    notes = Note.objects.all()
    return render(req,"index.html",context={'notes':notes})

def aboutview(req):
    return render(req,"about.html")

def detail_save(req):
    print(req.POST)
    title = req.POST.get("Title","")
    description = req.POST.get("Description","")
    
    if not title or not description:
        messages.error(req,"Fill all detils")
    else:
        messages.success(req, "Detail saved successfully")
        note = Note(Title=title, Description=description)
        note.save()
    
        
    return redirect("/")

def deleteview(req,id):
        note = Note.objects.get(id=id)
        note.delete()
        messages.success(req, "Detail deleted successfully")
        return redirect("/")
    
def edit_page(req,id):
    return render(req,'edit-page.html')
    
