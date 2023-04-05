from django.shortcuts import render, redirect
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

def home(request,blown):
    model_name_art = 'Blogentry'+blown
    Mart = apps.get_model(app_label='myapp',model_name=model_name_art)
    lname=request.session.get('lname',"")
    """
    if (isset($_COOKIE["isFlash"])) $flash= $_COOKIE["isFlash"]; else $flash=FALSE;
    """
    blogid=request.POST.get('blogid')
    entry=Mart.objects.filter(date=blogid).first()
    entry.delete()
    return redirect("/"+blown+"/blog")
    