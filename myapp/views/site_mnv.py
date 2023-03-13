from django.shortcuts import render
from django.utils.html import format_html
import os.path
import pathlib
from django.db import models

def home(request):
    return render(request,'site_mnv.html')
