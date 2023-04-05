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
#def home(request,blown,page=1):
def home(request,blown,theme):
    model_name_art = 'Blogentry'+blown
    model_name_com = 'Blogcomment'+blown
    model_name_thm = 'Blogthema'+blown
    Mart = apps.get_model(app_label='myapp',model_name=model_name_art)
    request.session['backafterreg'] = "/"+blown+"/blogth/theme"
    lname=request.session.get('lname',"")
    #selyear=request.POST.get("selyear","")
    allyears=Mart.objects.values_list('date',flat=True).order_by('-date')
    lyears = years.ylist(allyears)
    allthema=Mart.objects.values_list('thema',flat=True).order_by('-thema')
    lthema = thema.tlist(allthema)
    #perpage=8
    #pagedeb=(page-1)*perpage
    #pagefin=pagedeb+perpage
    #articles=Mart.objects.filter(thema__iregex=wthema).filter(date__startswith=stwith).order_by('-date')[pagedeb:pagefin]
    articles=Mart.objects.filter(thema=theme).order_by('-date')
    nbart=len(articles)
    titles=Mart.objects.values('date','what').filter(thema=theme).order_by('-date')
    target=blown+'/blogthm.html'
    param={'blown':blown,'lname':lname,'nbart':nbart,'entries':articles,'lthema':lthema,'lyears':lyears,'selyear':'Tous','selthem':theme,'titles':titles}
    return render(request,target,param)
