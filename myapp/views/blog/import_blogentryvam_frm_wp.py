from django.shortcuts import render
from django.utils.html import format_html
import os.path
import pathlib
import sqlite3
import re
from django.db import models
from myapp.models import Blogentryvam
from xml.dom import minidom

def home(request):
    # objs=Blogentryvam.objects.all().delete()
    listout=[]
    newhost="http://www.vivreaumanival.fr/static/uploads/legacy_wp/"
    legacy="https://vivreaumanival.files.wordpress.com/"
    exportfile="expfrmwp.xml"
    pagetitle="Create articles for vam blog from imported wordpress xml file - export file available at mysite/outfiles/"+exportfile
    
    file = minidom.parse('mysite/outfiles/'+exportfile)
    items = file.getElementsByTagName('item')
    for item in items:
        title=""
        if item.getElementsByTagName('title'):
            ntitle=item.getElementsByTagName('title')[0]
            if ntitle.childNodes:
                ti=ntitle.childNodes[0]
                title=ti.nodeValue
        #
        date=""
        if item.getElementsByTagName('wp:post_date'):
            npubdate=item.getElementsByTagName('wp:post_date')[0]
            pu=npubdate.childNodes[0]
            pubdate=pu.nodeValue
            date=pubdate.replace("-","").replace(" ","").replace(":","")
        #
        creator=""
        if item.getElementsByTagName('dc:creator'):
            ncreator=item.getElementsByTagName('dc:creator')[0]
            if ncreator.childNodes:
                cr=ncreator.childNodes[0]
                creator=cr.nodeValue
        #
        category=""
        if item.getElementsByTagName('category'):
            ncategory=item.getElementsByTagName('category')[0]
            category=ncategory.getAttribute('nicename')
            if not category or category=="uncategorized":
                category='divers'
        #
        content=""
        if item.getElementsByTagName('content:encoded'):
            ncontent=item.getElementsByTagName('content:encoded')[0]
            if ncontent.childNodes:
                ct=ncontent.childNodes[0]
                content=ct.nodeValue
        # --------------------------------------------------
        content=content.replace(legacy,newhost)
        #
        re5=re.compile('wp-image-([1-9][0-9]*)')
        nbs=re5.findall(content)
        for nb in nbs:
            content=content.replace('wp-image-'+nb,'wp-image')
        # 
        content=content.replace('<!-- wp:paragraph -->',"")
        content=content.replace('<!-- /wp:paragraph -->',"")
        content=content.replace("<p></p>","")
        content=content.replace("<p>&nbsp;</p>","")
        content=content.replace('<!-- wp:preformatted -->',"")
        content=content.replace('<!-- /wp:image -->',"")
        # ----------------------------------------------------
        if date != "" and title !="" and content != "": 
            obj=Blogentryvam.objects.create()
            obj.date=date
            obj.who=creator
            obj.what=title
            obj.thema=category
            obj.content=content
            obj.save()
        #
        listout.append(title+' ** '+date+' ** '+creator+' ** '+category+' ** '+content+'<br>')
    return render(request,'list.html',{'listout':listout,'title':pagetitle})
