import django
from django.contrib.auth.models import User
from django.conf import settings
from myapp.lib import night
import os
import dotenv

def set():
    #smtp_model='operator/smtpserv/port/username/pwd/ssl/tls'
    dotenv_file = os.path.join(settings.BASE_DIR,".env")
    if os.path.isfile(dotenv_file):
        dotenv.load_dotenv(dotenv_file)
    p = os.environ['smtp_params']
    params=p.split('/')
    mysmtp=params[1]
    myemail=params[3]
    #print("myemail ="+myemail)
    settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    settings.EMAIL_HOST=mysmtp
    settings.EMAIL_PORT=params[2]
    settings.EMAIL_HOST_USER=myemail
    settings.EMAIL_HOST_PASSWORD=night.dec(params[4])
    ssl=params[5]
    tls=params[6]
    if ssl == "True":
        settings.EMAIL_USE_SSL=True
    if tls == "True":
        settings.EMAIL_USE_TLS=True
    #settings.EMAIL_TIMEOUT=1
    settings.DEFAULT_FROM_EMAIL=myemail
    return 'OK'
