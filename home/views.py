from django.shortcuts import render,get_object_or_404
from .models import Contest,Problem,Con_signup,Contact
from login.models import User
from django.utils import timezone
import time
from django.http import HttpResponse
from django.apps import apps
from login.models import User
from django.apps import apps
from Compile_run.models import User_Problem

def get_u(request):
	try:
		u = request.session['user']
	except:
		return ''
	return u

def get_rank(user,contest_id):
	cont=apps.get_model(app_label='Leader', model_name="cont_"+str(contest_id))
	me = cont.objects.get(user=User.objects.get(id=user))
	all_users  = cont.objects.all()
	for rank,u in enumerate(all_users):
		if u == me:
			return rank+1


def contest(request):
	try:
		con=Contest.objects.all()
		con_signup = Con_signup.objects.filter(user=get_object_or_404(User,username=get_u(request)))
		contestlist=[]
		for x in con_signup:
			contestlist.append(x.contest)
	except Contest.DoesNotExist:
		raise Http404("contest does not exits")
	return render(request,'home/contest.html',{'con':con,'con_sign':contestlist})

def contest_details(request,contest_id):
	try:
		contest=Contest.objects.get(pk=contest_id)
		user = get_object_or_404(User,username=get_u(request))
		con_signup = Con_signup.objects.filter(user=get_object_or_404(User,username=get_u(request)))
		contestlist=[]
		for x in con_signup:
			contestlist.append(x.contest)
	except Contest.DoesNotExist:
		raise Http404("Contest does not exits")
	print('server')
	print((contest.start_time));
	print('client')
	print((timezone.now()));
	problems = Problem.objects.filter(Contest=contest)
	solved_status = []
	j = 1
	for i in problems:
		Us_Pro = User_Problem.objects.filter(User=user, Problem=i).first()
		if Us_Pro is None:
			solved_status.append(0)
		elif Us_Pro.status:
			solved_status.append(1)
		else :
			solved_status.append(2)
		j+=1
	print solved_status
	print(str(contest.end_time)[:16:]);
	if contest.start_time  <= timezone.now():
		return render(request,'home/contest_details.html',{'contest':contest,'end':str(contest.end_time)[:16:],'Rank':get_rank(user.id,contest.id),'problems_status':zip(problems,solved_status)})
	else :
		return render(request,'home/contest.html',{'con':Contest.objects.all(),'con_sign':contestlist})
	


def contest_info(request,contest_id):
	try:
		contest=Contest.objects.get(pk=contest_id)
		user = get_object_or_404(User,username=get_u(request))
	except Contest.DoesNotExist:
		raise Http404("Contest does not exits")
	problems = Problem.objects.filter(Contest=contest)
	solved_status = []
	j = 1
	for i in problems:
		Us_Pro = User_Problem.objects.filter(User=user, Problem=i).first()
		if Us_Pro is None:
			solved_status.append(0)
		elif Us_Pro.status:
			solved_status.append(1)
		else :
			solved_status.append(2)
		j+=1
	#print solved_status
	if contest.start_time  <= timezone.now():
		return render(request,'home/contest_details.html',{'contest':contest,'end':str(contest.end_time)[:16:],'Rank':get_rank(user.id,contest.id),'problems_status':zip(problems,solved_status)})
	else :
		return render(request,'home/con_signup.html',{'contest':contest,'end':str(contest.end_time)[:16:],'solved_status':solved_status})
	
def contest_signup(request,contest_id):
	print 'con_signup'
	try:
		contest=Contest.objects.get(pk=contest_id)
	except Contest.DoesNotExist:
		raise Http404("Contest does not exits")
	user = get_object_or_404(User,username=get_u(request))
	if Con_signup.objects.filter(contest=contest,user=user).first() is None :
		print 'signed up'
		con_signup=Con_signup(contest=contest,user=user,status=True)
		con_signup.save()
		cont_Leader=apps.get_model(app_label='Leader', model_name="cont_"+str(contest_id))
		new_rec = cont_Leader(user = user,sub_time=contest.start_time)
		new_rec.save()
	return render(request,'home/con_signup.html',{'contest':contest,'end':str(contest.end_time)[:16:]})

def logout(request):
	request.session['user'] = ''
	return render(request,'login/index.html')


def onsearch(request):
	if 	request.method == 'POST':
		keywords = request.POST.get('Keywords')
		res = Problem.objects.filter(p_name__contains=keywords)
		result = ''
		for i in res :
			result += i.p_name+'\n'
		print (str(result)) 	
		return HttpResponse(str(result))

def profile(request):
	data=get_object_or_404(User,username=get_u(request))
	return render(request,'home/profile.html',{'data':data})

def profileUpdate(request):
	data=get_object_or_404(User,username=get_u(request))
	data.clgname=request.POST.get('clgname')
	data.languages=request.POST.get('languages')
	data.experience=request.POST.get('experience')
	data.save()
	return render(request,'home/profile.html',{'data':data})

def contactPage(request):
	return render(request,'home/contact.html')

def contact(request):
	if request.method=='POST':
		fd=Contact(name=request.POST.get('name'),email=request.POST.get('email'),sub=request.POST.get('sub'),message=request.POST.get('message'))
		fd.save()
		msg='success'
		return HttpResponse(msg)
	else:
		return HttpResponse("fail")
