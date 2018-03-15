from django.conf.urls import url,include
from . import views
app_name='login'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^signup/$',views.signup,name='signup'),
    url(r'^signin/$',views.signin,name='signin'),
    url(r'^forgot/$',views.forgot,name='forgot'),
]