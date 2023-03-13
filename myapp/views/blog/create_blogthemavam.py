from django.shortcuts import render
from django.utils.html import format_html
import os.path
import pathlib
import sqlite3
import csv
from django.db import models
from myapp.models import Flashjdu

def home(request):
    #conx = sqlite3.connect('db.sqlite3')
    #c=conx.cursor()
    #c.execute("DROP TABLE IF EXISTS myapp_flashjdu")
    #conx.commit()
    #conx.close()
    objs=Flashjdu.objects.all().delete()
    csv.register_dialect('csv_dialect',
                    delimiter='|',
                    skipinitialspace=True,
                    quoting=csv.QUOTE_NONE)
    listout=[]
    with open('flashsjdu.csv') as csvfile:
        reader=csv.reader(csvfile, dialect='csv_dialect')
        for line in reader:
                obj=Flashjdu.objects.create()
                obj.date=line[1]
                obj.author=line[2]
                obj.content=line[3]
                obj.save()
                listout.append(line[1]+' ** '+line[3])
    return render(request,'list.html',{'listout':listout,'title':'Create News from .csv file'})