from django.shortcuts import render
from django.utils.html import format_html
import os.path
import pathlib
import sqlite3
import csv
from django.db import models
from myapp.models import Blogentryvam

def home(request):
    objs=Blogentryvam.objects.all().delete()
    csv.register_dialect('csv_dialect',
                    delimiter='|',
                    skipinitialspace=True,
                    quoting=csv.QUOTE_NONE)
    listout=[]
    with open('mysite/outfiles/blogentryvam.csv') as csvfile:
        reader=csv.reader(csvfile, dialect='csv_dialect')
        for line in reader:
                obj=Blogentryjdb.objects.create()
                obj.date=line[1]
                obj.who=line[2]
                obj.what=line[3]
                obj.thema=line[4]
                obj.content=line[5]
                obj.save()
                listout.append(line[1]+' ** '+line[5])
    return render(request,'list.html',{'listout':listout,'title':'Create Blog entry vam from .csv file'})