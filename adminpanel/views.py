from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from home.models import Contest,Problem
from Compile_run.models import TestCase
from django.http import Http404
from django.contrib.auth import authenticate,login
from Compile_run.models import Problem_session
from login.models import User,AdminUser
from Compile_run.views import getWelO
from home.views import get_u

def index(request):
	get_object_or_404(AdminUser,user=get_object_or_404(User,username=get_u(request)))
	data=Contest.objects.all();
	return render(request,'adminpanel/addqus.html',{'data':data})
def details(request):
	return render(request,'adminpanel/details.html')

def addcon(request):
	if request.method=='POST':
		form=Contest(con_name=request.POST.get('name'),con_date=request.POST.get('start_time')[:10:],start_time=request.POST.get('start_time'),start=request.POST.get('start_time'),end_time=request.POST.get('end_time'),end=request.POST.get('end_time'),org_name=request.POST.get('org_name'),image=request.POST.get('image'),tagline=request.POST.get('tagline'),disc=request.POST.get('disc'),rules=request.POST.get('rules'),prize=request.POST.get('prize'),scoring=request.POST.get('scoring'))
		form.save()
		data=Contest.objects.all();
		return render(request,'adminpanel/addqus.html',{'data':data})

def showqus(request,con_id):
	return render(request,'adminpanel/showqus.html',{'con_id':con_id})

def addqus(request):
	if request.method=='POST':
		con_id=request.POST.get('id')
		contest=Contest.objects.get(id=con_id)
		form=Problem(Contest=contest,p_name=request.POST.get('problem'),score=request.POST.get('marks'),p_level=request.POST.get('level'),p_disc=request.POST.get('disc'),p_input=request.POST.get('input'),p_cons=request.POST.get('cons'),p_output=request.POST.get('output'),sample_input=getWelO(request.POST.get('sample_input')),sample_output=getWelO(request.POST.get('sample_output')),exp=request.POST.get('exp'))
		form.save()
		data=Contest.objects.all();
		return render(request,'adminpanel/addqus.html',{'data':data})

def allqus(request,con_id):
	if request.method=='POST':

		try:
			data=Problem.objects.filter(Contest=Contest.objects.get(id=con_id))
			print (data)
		except Problem.DoesNotExist:
			raise Http404("Problems does not exits")
		return render(request,'adminpanel/allqus.html',{'data':data})

def addtest(request,p_id):
	return render(request,'adminpanel/addtest.html',{'problem':Problem.objects.get(id=p_id)})

def savetest(request,p_id):
	problem=Problem.objects.get(id=p_id)
	tc=TestCase(Problem=problem,testin=getWelO(request.POST.get('input')),testout=getWelO(request.POST.get('output')),weight=request.POST.get('weight'))
	tc.save()
	return render(request,'adminpanel/addtest.html',{'problem':Problem.objects.get(id=p_id)})

def addsession(request,p_id):
	return render(request,'adminpanel/addsession.html',{'problem':Problem.objects.get(id=p_id)})

def savesession(request,p_id):
	if request.method == 'POST':
		problem = Problem.objects.get(id=p_id)
		if Problem_session.objects.filter(Problem=problem).first() is None:
			p_ses = Problem_session(Problem=problem,c_session_code=request.POST.get('c'),cpp_session_code=request.POST.get('cpp'),java_session_code=request.POST.get('java'),py_session_code=request.POST.get('python'))
			p_ses.save()
		else:
			p_ses = Problem_session.objects.get(Problem=problem)
			p_ses.c_session_code = request.POST.get('c')
			p_ses.cpp_session_code = request.POST.get('cpp')
			p_ses.java_session_code = request.POST.get('java')
			p_ses.py_session_code = request.POST.get('python')
			p_ses.py_session_code = request.POST.get('python3')
			p_ses.save()
		data=Contest.objects.all();
		return render(request,'adminpanel/addqus.html',{'data':data})
