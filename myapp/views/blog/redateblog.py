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

@csrf_exempt
def home(request,blown):
    model_name_art = 'Blogentry'+blown
    Mart = apps.get_model(app_label='myapp',model_name=model_name_art)
    request.session['backafterreg'] = "/"+blown+"/blog/"
    lname=request.session.get('lname',"")
    articles=Mart.objects.order_by('-date').all()
    nbart=len(articles)
    target='blog/redateblog.html'
    param={'blown':blown,'entries':articles}
    return render(request,target,param)

def change(request,blown,id):
    model_name_art = 'Blogentry'+blown
    Mart = apps.get_model(app_label='myapp',model_name=model_name_art)
    request.session['backafterreg'] = "/"+blown+"/blog/"
    lname=request.session.get('lname',"")
    article=Mart.objects.get(id=int(id))
    article.date=request.POST.get('date')
    article.save()
    articles=Mart.objects.order_by('-date').all()
    target='blog/redateblog.html'
    param={'blown':blown,'entries':articles}
    return render(request,target,param)
