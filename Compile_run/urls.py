"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from . import views


app_name = 'Compile_run'
'''
app_name is added bcoz name of 
'''
urlpatterns = [
    url (r'^(?P<problem_name>[0-9A-Za-z_]+)/$',views.index,name='index'),
    url (r'^run/(?P<problem_id>[0-9]+)/', views.run, name='run'),
    url (r'^submit/(?P<problem_id>[0-9]+)/', views.submit, name='submit'),
    url (r'^change/(?P<problem_id>[0-9]+)/', views.change, name='change'),
    url (r'^code/(?P<problem_id>[0-9]+)/(?P<sub_id>[0-9]+)/', views.code, name='code'),
]
