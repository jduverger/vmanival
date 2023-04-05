import django
from django.contrib.auth.models import User
from django.conf import settings
from myapp.lib import night

def set():
    myemail='jduvr@orange.fr'
    mysmtp='smtp.orange.fr'
    user=User.objects.get(username=mysmtp)
    settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    settings.EMAIL_HOST=mysmtp
    settings.EMAIL_PORT=465
    settings.EMAIL_HOST_USER=myemail
    settings.EMAIL_HOST_PASSWORD=night.dec(user.first_name)
    settings.EMAIL_USE_SSL=True
    settings.EMAIL_USE_TLS=False
    #settings.EMAIL_TIMEOUT=1
    settings.DEFAULT_FROM_EMAIL=myemail
    return 'OK'
