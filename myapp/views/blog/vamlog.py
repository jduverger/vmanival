from django.shortcuts import redirect
from django.utils.html import format_html
import os.path
import pathlib

def home(request):
    return redirect('/jdb/blog')
