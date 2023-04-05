from django.shortcuts import render
from django.utils.html import format_html
import os.path
import pathlib
import sqlite3
from django.apps import apps
from django.db import models
from myapp.models import Blogentryvam
from xml.dom import minidom

def home(request,blown,oldt,newt):
    model_name_art = 'Blogentry'+blown
    Mart = apps.get_model(app_label='myapp',model_name=model_name_art)
    articles=Mart.objects.all()
    for entry in articles:
        if (not entry.thema) or entry.thema =="": 
            entry.thema="a_trier"
            entry.save()
        if entry.thema == oldt:
            entry.thema=newt
            entry.save()
    listout=""        
    return render(request,'list.html',{'listout':listout,'title':'Change category from= '+oldt+' to= '+newt})
