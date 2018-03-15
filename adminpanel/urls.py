from django.conf.urls import url,include
from . import views
app_name='adminpanel'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^details/$',views.details,name='details'),
    url(r'^addcon/$',views.addcon,name='addcon'),
    url(r'^(?P<con_id>[0-9]+)/$',views.showqus,name='showqus'),
    url(r'^addqus/$',views.addqus,name='addqus'),
    url(r'^allqus/(?P<con_id>[0-9]+)/$',views.allqus,name='allqus'),
    url(r'^addtest/(?P<p_id>[0-9]+)/$',views.addtest,name='addtest'),
    url(r'^savetest/(?P<p_id>[0-9]+)/$',views.savetest,name='savetest'),
    url(r'^savesession/(?P<p_id>[0-9]+)/$',views.savesession,name='savesession'),
    url(r'^addsession/(?P<p_id>[0-9]+)/$',views.addsession,name='addsession'),
]