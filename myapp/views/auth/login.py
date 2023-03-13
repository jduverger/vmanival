from django.shortcuts import render, redirect
from django.utils.html import format_html
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

import os.path
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    backafterreg=request.session['backafterreg']
    target='auth/login.html'
    param={'title':'Saisir vos coordonnees','backafterreg':backafterreg}
    return render(request,target,param)

def check(request):
    backafterreg=request.session['backafterreg']
    #user = authenticate(username=request.POST['username'],password=)
    user=User.objects.get(username=request.POST['username']).check_password(request.POST['password'])
    if user is None :
        home(request)
    request.session['lname']=request.POST['username']
    return redirect(backafterreg) 

def logout(request):
    backafterreg=request.session['backafterreg']
    del request.session['lname']
    return redirect(backafterreg)
