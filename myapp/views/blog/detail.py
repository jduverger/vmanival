from django.shortcuts import render
from django.utils.html import format_html
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

from django.apps import apps
import os.path
import pathlib
import sqlite3
import datetime
from django.db import models
from myapp.lib import years
from myapp.lib import thema

@xframe_options_exempt
def home(request,blown,blogid):
    model_name_art = 'Blogentry'+blown
    model_name_com = 'Blogcomment'+blown
    model_name_thm = 'Blogthema'+blown
    lname=request.session.get('lname',"")
    retour=blown+"/blog"
    Mart = apps.get_model(app_label='myapp',model_name=model_name_art)
    article=Mart.objects.filter(date=blogid).order_by('-date').first()
    target='vam/gen.html'
    param={'blown':blown,'lname':lname,'entry':article,'blogid':blogid,'incl':'blog/incl_onearticle.html'}
    return render(request,target,param)
"""
	$comments=$this->comments->where('blogid','=',$blogid)->get();
"""
