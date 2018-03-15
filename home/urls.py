from django.conf.urls import url,include
from . import views
app_name='home'
urlpatterns = [
    url(r'^$',views.contest,name='contest'),
    url(r'^(?P<contest_id>[0-9]+)/contest_details/$',views.contest_details,name='contest_details'),
    url(r'^(?P<contest_id>[0-9]+)/contest_info/$',views.contest_info,name='contest_info'),
    #url(r'^problem/(?P<problem_id>[0-9]+)/$',views.problem,name='problem'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^onsearch/$',views.onsearch,name='onsearch'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^profileupdate/$',views.profileUpdate,name='profileUpdate'),
    url(r'^(?P<contest_id>[0-9]+)/contest_signup/$',views.contest_signup,name='contest_signup'),
    url(r'^contact_us/$',views.contactPage,name='contactPage'),
    url(r'^contact/$',views.contact,name='contact'),
]
