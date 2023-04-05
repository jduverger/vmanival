from django.urls import include, path

#from myapp.views.blog import vamlog
from myapp.views.blog import create_blogentryvam
from myapp.views.blog import blog
from myapp.views.blog import blogthm
from myapp.views.blog import detail
from myapp.views.blog import newart
from myapp.views.blog import insart
from myapp.views.blog import delart
from myapp.views.blog import editart
from myapp.views.blog import redateblog
from myapp.views.blog import import_blogentryvam_frm_wp
from myapp.views.blog import chg_blogentry_category
from myapp.views.blog import drop_blogentryvam_tbl

urlpatterns = [
    path('create_blogentryvam',create_blogentryvam.home),
    path('drop_artvam_tbl',drop_blogentryvam_tbl.home),
    path('imp_artvam_frm_wp',import_blogentryvam_frm_wp.home),
    path('<str:blown>/blog',blog.home),
    path('<str:blown>/blog/',blog.home),
    path('<str:blown>/blog/last',blog.last),
    path('<str:blown>/blog/<int:page>',blog.home),
    path('<str:blown>/blogthm/<str:theme>',blogthm.home),
    path('<str:blown>/blog/detail/<str:blogid>',detail.home),
    path('<str:blown>/blog/newart',newart.home),
    path('<str:blown>/blog/insart',insart.home),
    path('<str:blown>/blog/editart/<str:blogid>',editart.home),
    path('<str:blown>/blog/delart/',delart.home),
    path('<str:blown>/redateblog/',redateblog.home),
    path('<str:blown>/redateblog/change/<int:id>',redateblog.change),
    path('<str:blown>/chg_blogentry_category/<str:oldt>/<str:newt>',chg_blogentry_category.home),

    #legacy
    #path('vamblog',vamblog.home),
    #path('index.php/<str:blown>/blog',vamblog.home),
]
