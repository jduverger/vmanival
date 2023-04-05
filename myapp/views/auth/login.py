from django.shortcuts import render, redirect
from django.utils.html import format_html
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from myapp.lib import smtp
import os.path
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    ok=smtp.set()
    backafterreg=request.session['backafterreg']
    target='auth/login.html'
    param={'title':'Saisir vos coordonnees','backafterreg':backafterreg}
    return render(request,target,param)

def check(request):
    backafterreg=request.session['backafterreg']
    lname=request.POST['username']
    pwd=request.POST['password']
    if not lname or not pwd:
        backafterreg=request.session['backafterreg']
        target='auth/login.html'
        param={'title':'Saisir vos coordonnees','backafterreg':backafterreg}
        return render(request,target,param)
    user = authenticate(username=lname, password=pwd)
    if user is not None:
        request.session['lname']=request.POST['username']
        return redirect(backafterreg)
    backafterreg=request.session['backafterreg']
    target='auth/login.html'
    param={'title':'Saisir vos coordonnees','backafterreg':backafterreg}
    return render(request,target,param)

def logout(request):
    backafterreg=request.session['backafterreg']
    del request.session['lname']
    return redirect(backafterreg)
