from . import  views
from django.conf.urls import url

app_name='Leader'

urlpatterns = [
    url(r'^create/(?P<cont_id>[0-9]+)$',views.index,name='index'),
    url(r'^(?P<cont_id>[0-9]+)$',views.leader ,name='leader'),
    url(r'(?P<uname>[0-9A-Za-z_]+)$',views.get_user,name='user'),
]
