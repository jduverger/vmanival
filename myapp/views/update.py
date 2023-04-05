from django.shortcuts import render,redirect
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
from django.db import connection
#from myapp.models import Maintenboat

@csrf_exempt
def home(request):
    lname=request.session.get('lname',"")
    if lname == "":
        target="accessdenied.html"
        return render(request,target)
    #
    retour=request.POST['retour']
    scrollpos=request.POST.get('scrollpos')
    tname=request.POST.get('table')
    id=request.POST.get('id')
    # mod=tname.capitalize()
    # MyModel=apps.get_model("myapp",mod)
    table="myapp_"+tname
    field=request.POST.get('field')
    value=request.POST.get('value')
    SQL="UPDATE "+table+" SET "+field+"='"+value+"' WHERE id ="+id
    #print(SQL)
    with connection.cursor() as cursor:
        cursor.execute(SQL)
    return redirect("/"+retour+"/"+str(scrollpos)+"/"+str(id))

def delete(request):
    lname=request.session.get('lname',"")
    if lname == "":
        target="accessdenied.html"
        return render(request,target)
    #
    retour=request.POST.get('retour')
    scrollpos=request.POST.get('scrollpos')
    tname=request.POST.get('table')
    id=request.POST.get('id')
    # mod=tname.capitalize()
    # MyModel=apps.get_model("myapp",mod)
    table="myapp_"+tname
    SQL="DELETE FROM "+table+" WHERE id ="+id
    print(SQL)
    with connection.cursor() as cursor:
        cursor.execute(SQL)
    return redirect("/"+retour+"/"+str(scrollpos)+"/"+str(id))