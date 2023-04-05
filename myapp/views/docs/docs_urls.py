from django.urls import include, path

from myapp.views.docs import pubdoc
from myapp.views.docs import mngdocs

urlpatterns=[
    path('pubdoc',pubdoc.home),
    path('uplpub',mngdocs.uplpub),
    path('uplpriv',mngdocs.uplpriv),
    path('delpub',mngdocs.delpub),
    path('delpriv',mngdocs.delpriv),
    path('mngdocs',mngdocs.home),
]
