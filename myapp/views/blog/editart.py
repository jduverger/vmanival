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
import time
from django.db import models
from myapp.lib import thema
from myapp.lib import compdate

def home(request,blown,blogid):
	model_name_art='Blogentry'+blown
	Mart=apps.get_model(app_label='myapp',model_name=model_name_art)
	lname=request.session.get('lname',"")
	allthema=Mart.objects.values_list('thema',flat=True).order_by('-thema')
	lthema=thema.tlist(allthema)
	entry=Mart.objects.filter(date=blogid).first()
	target=blown+'/gen.html'
	incl='blog/incl_editart.html'
	param={'blown':blown,'blogid':blogid,'lname':lname,'entry':entry,'lthema':lthema,'incl':incl}
	return render(request,target,param)
