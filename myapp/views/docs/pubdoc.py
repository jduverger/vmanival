from django.shortcuts import render, redirect
from django.utils.html import format_html
from django.http import HttpResponse
from django.apps import apps
from django.conf import settings
import os
import os.path
import pathlib

def home(request):
    media=settings.MEDIA_ROOT
    path=media+"/docs/pub/"
    docs=os.listdir(path)
    ldocs={}
    for doc in docs:
        filename,filex=os.path.splitext(doc)
        if filex in [".pdf",".PDF"]:
            ldocs[doc]=request.build_absolute_uri("/media/docs/pub/"+doc)
    param={'ldocs':ldocs}
    return render(request,'docs/pubdoc.html',param)