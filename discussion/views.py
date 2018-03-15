from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from login.models import User
from home.models import Contest,Problem
import datetime
from .models import Discussion
from login.models import User
from django.apps import apps

from channels import Group
from home.views import get_u


def get_rank(user,contest_id):
	cont=apps.get_model(app_label='Leader', model_name="cont_"+str(contest_id))
	me = cont.objects.get(user=User.objects.get(id=user))
	all_users  = cont.objects.all()
	for rank,u in enumerate(all_users):
		if u == me:
			return rank+1

def disc(request,contest_id):
	contest=Contest.objects.get(id=contest_id)
	user=get_object_or_404(User,username=get_u(request))
	return render(request,'discussion/forum.html',{'All':Discussion.objects.filter(contest=contest).order_by('-id'),'contest_id':contest_id,'contest':contest,'end':str(contest.end_time)[:16:],'Rank':get_rank(user.id,contest.id)})


def addcom(request):
	user=User.objects.filter(username=get_u(request)).first()
	con = request.POST.get('con')
	contest=Contest.objects.get(id=con)
	message = request.POST.get('comment')
	
	time = datetime.datetime.now().replace(microsecond=0)
	
	discussion = Discussion(user=user,contest=contest,message=message,time=time)
	discussion.save()
	con_name=contest.con_name.replace(" ","_")
    
	Group(con_name).send({'text': '<div class="comment"><div class="content"><a class="author">'+str(discussion.user.username)+'</a><div class="metadata"><div class="date">'+str(discussion.time)+'</div></div><pre class="ui segment" style="background-color: #f8f8f8;border:0px;">'+str(discussion.message)+'</pre></div></div>'})
	return HttpResponse("success")


def delcom(request):
	com=request.POST.get('com')
	Discussion.objects.filter(id=com).delete()
	return HttpResponse("success")




