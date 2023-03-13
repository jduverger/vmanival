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
from myapp.lib import thema
from myapp.lib import compdate

def home(request,blown,page=1):
    model_name_art = 'Blogentry'+blown
    model_name_com = 'Blogcomment'+blown
    Mart = apps.get_model(app_label='myapp',model_name=model_name_art)
    lname=request.session.get('lname',"")
    allthema=Mart.objects.values_list('thema',flat=True).order_by('-thema')
    lthema = thema.tlist(allthema)
    blogid=compdate.datim()
    titles="Entrez un nouvel article"
    target=blown+'/gen.html'
    param={'blown':blown,'page':page,'lname':lname,'blogid':blogid,'lthema':lthema,'titles':titles,'incl':'blog/incl_newart.html'}
    return render(request,target,param)
