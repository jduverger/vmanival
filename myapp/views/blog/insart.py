from django.shortcuts import render, redirect
from django.utils.html import format_html
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
from django.conf import settings

from django.apps import apps
import os.path
import pathlib
import sqlite3
import datetime
import base64
import os
from django.db import models
from PIL import Image
from myapp.lib import compdate
from myapp.lib import formatdoc

def imgsize(W,H):
	maxw=1000
	maxh=800
	neww=W
	newh=H
	if W > H:	#horizontal
		if W > maxw:
			newh=int(H*(maxw/W))
			neww=maxw
	else:		#vertical
		if H > maxh:
			neww=int(W*(maxh/H))
			newh=maxh
	return neww,newh

def home(request,blown):
	lname=request.session.get('lname',"")
	model_name_art = 'Blogentry'+blown
	Mart = apps.get_model(app_label='myapp',model_name=model_name_art)
	blogid=request.POST.get('blogid')
	entry=Mart.objects.filter(date=blogid).first()
	if entry == None:
		entry=Mart.objects.create()
	entry.date=blogid
	entry.who=request.POST.get('who')
	entry.what=request.POST.get('what')
	entry.thema=request.POST.get('thema')
	entry.content=request.POST.get('content')
	entry.save()
	#
	code_action=request.POST.get('code_action')
	selection=request.POST.get('cursor_pos')
	pos_img=request.POST.get('posimg')
	print("code_action="+code_action)
	print("selection="+selection)
	print("pos_img="+pos_img)
	#----------------------------------
	if code_action == "register":
		return redirect("/"+blown+'/blog')
	#---------------------------------
	if code_action == "imgload":
		if request.method == 'POST':
			dPath=os.path.join(settings.BASE_DIR,"static")+"/uploads/"
			# ex: /home/newoueb/nwsite/static/uploads/
			myfile=request.FILES['mydoc']
			orifname=myfile.name
			imgfile=myfile.file
			myimg=Image.open(myfile)
			W,H=myimg.size
			nsize=imgsize(W,H)
			neww=nsize[0]
			newh=nsize[1]
			myimg=myimg.resize((neww,newh),Image.ANTIALIAS)
			myimg.save(dPath+blown+"_"+orifname,optimize=True,quality=85)
			fpath = request.build_absolute_uri('/static/uploads/')+blown+"_"+orifname
			# ex: fpath http://newoueb.eu.pythonanywhere.com/static/uploads/jdb_img001.jpg
			#code=formatdoc.attachref(orifname,neww,newh,fpath)
			code=formatdoc.attachref(orifname,fpath,pos_img)
			content=entry.content
			#
			if selection != 0 and selection !="" :
				pos=content.find(selection)
				if pos >= 0:
					content = content[:pos]+code +content[pos:]
				else:
					content=content+code
			else:
				content=content+code
			#
			entry.content=content
			entry.save()
		return redirect("/"+blown+'/blog/editart/'+blogid)
	else:
		print("no action! code_action="+code_action)
