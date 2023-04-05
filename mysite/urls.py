"""mysite URL Configuration
"""
from django.contrib import admin
from django.contrib import auth
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt

from myapp.views.auth import login
from myapp.views import update
from myapp.views import adhesion
from myapp.views import site_mnv

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),

    path('',TemplateView.as_view(template_name='welcome.html'),name='welcome'),
    path('welcome/',TemplateView.as_view(template_name='welcome.html'),name='welcome'),
    path('',TemplateView.as_view(template_name='accessdenied.html')),
    path('login/',login.home),
    path('logout/',login.logout),
    path('login/check/',login.check),
#
    path('adherer',adhesion.home),
    path('site_mnv',site_mnv.home),
#    path('menuprv/',menuprv.home),
    path('update/',update.home),
    path('delete/',update.delete),
    path('', include('myapp.views.blog.blog_urls')),
    path('', include('myapp.views.docs.docs_urls')),
]
