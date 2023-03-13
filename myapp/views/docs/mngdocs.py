from django.shortcuts import render, redirect
from django.utils.html import format_html
from django.http import HttpResponse
from django.apps import apps
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
import os.path
import pathlib
import time

def home(request):
    lname=request.session.get('lname',"")
    request.session['backafterreg'] = "/mngdocs"
    if lname =="":
        return redirect('/login/')

    media=os.path.join(settings.BASE_DIR,"media")
    path=media+"/docs/pub/"
    docs=os.listdir(path)
    cdocs={}
    ct={}
    for doc in docs:
        filename,filex=os.path.splitext(doc)
        if filex in [".pdf",".PDF"]:
            cdocs[doc]=request.build_absolute_uri("/media/docs/pub/"+doc)
            ct[doc]=time.ctime(os.path.getmtime(path+doc))
    
    path=media+"/docs/priv/"
    docs=os.listdir(path)
    adocs={}
    at={}
    for doc in docs:
        filename,filex=os.path.splitext(doc)
        if filex in [".pdf",".PDF"]:
            adocs[doc]=request.build_absolute_uri("/media/docs/priv/"+doc)
            at[doc]=time.ctime(os.path.getmtime(path+doc))
    
    param={'cdocs':cdocs,'ct':ct,'adocs':adocs,'at':at}
    return render(request,'docs/mngdocs.html',param)

def delpub(request):
    raz=request.POST.get("raz")
    doc=request.POST.get("doc")
    if raz:
        media=os.path.join(settings.BASE_DIR,"media")
        os.unlink(media+"/docs/pub/"+doc)
    return redirect('/mngdocs')

def delpriv(request):
    raz=request.POST.get("raz")
    doc=request.POST.get("doc")
    if raz:
        media=os.path.join(settings.BASE_DIR,"media")
        os.unlink(media+"/docs/priv/"+doc)
    return redirect('/mngdocs')

def uplpub(request):
    myfile=request.FILES['mydoc']
    media=os.path.join(settings.BASE_DIR,"media")
    fs = FileSystemStorage(location=media+'/docs/pub')
    filename = fs.save(myfile.name, myfile)
    return redirect('/mngdocs')

def uplpriv(request):
    myfile=request.FILES['mydoc']
    media=os.path.join(settings.BASE_DIR,"media")
    fs = FileSystemStorage(location=media+'/docs/priv')
    filename = fs.save(myfile.name, myfile)
    return redirect('/mngdocs')
