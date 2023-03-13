from django.db import models

# Create your models here.
class Blogentryvam(models.Model):
    date = models.CharField(max_length=15,null=True,default="")
    who = models.CharField(max_length=50,null=True,default="")
    what = models.CharField(max_length=50,null=True,default="")
    thema = models.CharField(max_length=25,null=True,default="")
    content = models.TextField(null=True,default="")

class Blogcommentvam(models.Model):
    blogid = models.CharField(max_length=15,null=True,default="")
    date = models.CharField(max_length=15,null=True,default="")
    who = models.CharField(max_length=50,null=True,default="")
    what = models.CharField(max_length=50,null=True,default="")
    content = models.TextField(null=True,default="")

