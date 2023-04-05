from django.shortcuts import render
from django.utils.html import format_html
import os.path
import pathlib
import sqlite3
from django.db import models
from myapp.models import Blogentryvam
from xml.dom import minidom

def home(request):
    objs=Blogentryvam.objects.all().delete()
    listout=[]
    return render(request,'list.html',{'listout':listout,'title':'Drop blogentryvam table'})
