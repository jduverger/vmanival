from django.shortcuts import redirect
from django.utils.html import format_html
import os.path
import pathlib

def home(request):
    return redirect('http://www.newoueb.com/index.php/vam/blog')
def detail(request,numart):
    return redirect('http://www.newoueb.com/index.php/vam/blog/detail/'+numart)
