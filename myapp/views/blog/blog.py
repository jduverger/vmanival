from django.shortcuts import render
from django.utils.html import format_html
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt

from django.apps import apps
import os.path
import pathlib
import sqlite3
import datetime
from django.db import models
from myapp.lib import years
from myapp.lib import thema
from myapp.lib import dispdate

@csrf_exempt
def home(request,blown,page=1):
    model_name_art = 'Blogentry'+blown
    model_name_com = 'Blogcomment'+blown
    model_name_thm = 'Blogthema'+blown
    Mart = apps.get_model(app_label='myapp',model_name=model_name_art)
    request.session['backafterreg'] = "/"+blown+"/blog/"
    lname=request.session.get('lname',"")
    selyear=request.POST.get("selyear","")
    if selyear == "" or selyear== "Tous":
        stwith="2"
        selyear="Tous"
    else:
        stwith=selyear
    selthem=request.POST.get("selthem","")
    if selthem == "" or selthem == "Tous":
        wthema=".*"
        selthem="Tous"
    else:
        wthema=selthem
    allyears=Mart.objects.values_list('date',flat=True).order_by('-date')
    lyears = years.ylist(allyears)
    allthema=Mart.objects.values_list('thema',flat=True).order_by('-thema')
    lthema = thema.tlist(allthema)
    perpage=8
    pagedeb=(page-1)*perpage
    pagefin=pagedeb+perpage
    articles=Mart.objects.filter(thema__iregex=wthema).filter(date__startswith=stwith).order_by('-date')[pagedeb:pagefin]
    nbart=len(articles)
    titles=Mart.objects.values('date','what').filter(thema__iregex=wthema).filter(date__startswith=stwith).order_by('-date')
        
    target=blown+'/blog.html'
    param={'blown':blown,'page':page,'lname':lname,'nbart':nbart,'entries':articles,'lthema':lthema,'lyears':lyears,'selyear':selyear,'selthem':selthem,'titles':titles}
    return render(request,target,param)

def last(request,blown):
    model_name='Blogentry'+blown
    Mpost=apps.get_model(app_label='myapp',  model_name=model_name)
    post=Mpost.objects.order_by('-date').first()
    date=dispdate.fdd(post.date)
    what=post.what
    text="Dernier article : <span style='color:red;'>"+date+" - "+what+"</span>"
    response = HttpResponse(text)
    response['content-type']="application/xml; charset=utf-8"
    response["Access-Control-Allow-Origin"]="*"
    response["Vary"]="Origin"
    return response
