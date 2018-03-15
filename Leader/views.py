from django.shortcuts import render,get_object_or_404
from login.models import User
from home.models import Contest,Problem
from django.db import models
from . import create
from django.apps import apps
from .apps import LeaderConfig
#from .create import *
import importlib
 #from .models import cont_1
from login.models import User
from django.apps import apps
from home.views import get_u




def get_rank(user,contest_id):
	cont=apps.get_model(app_label='Leader', model_name="cont_"+str(contest_id))
	me = cont.objects.get(user=User.objects.get(id=user))
	all_users  = cont.objects.all()
	for rank,u in enumerate(all_users):
		if u == me:
			return rank+1

def index(request,cont_id):
    name="cont_"+str(cont_id)
    p_ids=Problem.objects.filter(Contest=cont_id)
    contest=Contest.objects.get(id=cont_id)
    new_class=create.createmodel(name,p_ids)
    return render(request,'Leader/remainder.html',{'vvt':new_class,'contest':contest})

def leader(request,cont_id):
    cont=apps.get_model(app_label='Leader', model_name="cont_"+str(cont_id))

    meta = create.splitm(cont._meta.get_fields())

    contest_temp = Contest.objects.get(id=cont_id)

    time = contest_temp.start_time
    contest=Contest.objects.get(id=cont_id)
    time = time.replace(microsecond = 0)
    res=cont.objects.all()
    events=create.get_table(res,meta,time)
    user = get_object_or_404(User,username=get_u(request))
    #field=cont._meta.fields()
    meta[0] = 'Rank'
    meta[1] = 'User'
    meta[2] = 'Time'
    meta[3] = 'Score'
    return render(request,'Leader/index.html',{'participents':events,'fields':meta,'cont_id':cont_id, 'time':time,'contest':contest,'end':str(contest.end_time)[:16:],'Rank':get_rank(user.id,contest.id)})

def add_user(request,cont_id,user_name):
    cont=apps.get_model(app_label='Leader', model_name="cont_"+str(cont_id))
    user_obj=User.objects.get(name=user_name)
    contest=Contest.objects.get(id=cont_id)
    a=cont(user=user_obj)
    a.save()
    return  render(request,'Leader/index.html')

def get_user(request,uname):
    obj=User.objects.get(username=uname)
    return render(request,'Leader/index.html',{'vvt':obj.username})

