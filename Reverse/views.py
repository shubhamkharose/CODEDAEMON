from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from Compile_run.models import User_Problem,TestCase,Problem_session,AdminSettings
import subprocess
from django.template import loader
import datetime
from threading import Thread
import time
import json
from home.models import Problem,Contest
from login.models import User 
from django.apps import apps
from Leader import create,views
import select
from login.models import User
from django.apps import apps
from django.utils.html import escape
import signal,os
from signal import SIG_DFL
from .models import Reverse
from Compile_run.views import get_rank

from home.views import get_u

def getWelO(ans):
	s1 = ans.split("\n")
	s2 = []
	
	for string in s1 :
		string = string.strip(" ")
		string = string.strip("\r")
		if string is "\n" or string == '':
			continue
		s2.append(string)
	ans = '\n'.join(s2)
	return ans

def getO(command,timeout):	
	poll_obj = select.poll()
	poll_obj.register(command.stdout, select.POLLIN)
	buflimit = AdminSettings.objects.get(id=1).buff
	buf = 0
	ans =''
	start = time.time()
	idealbuffer =1
	while buf <= buflimit and start + timeout > time.time() : 
		poll_result = poll_obj.poll(0)
		if poll_result:
			ans+= command.stdout.read(idealbuffer)
			buf+=idealbuffer
	return getWelO(ans)



def index(request,problem_name):
	problem = Problem.objects.get(p_name=problem_name)
	R_problem = Reverse.objects.get(Problem=problem)
	contest = problem.Contest
	session = Problem_session.objects.get(Problem=problem).c_session_code
	user=get_object_or_404(User,username=get_u(request))

	Us_Pro = User_Problem.objects.filter(User=user, Problem=problem).first()

	Submission = apps.get_model(app_label='Leader', model_name="Sub_cont_"+str(problem.Contest.id))
	all_sub=Submission.objects.filter(User=user,Problem=problem)
	meta = ['id','time','pts','Lang']
	time = contest.start_time
	time = time.replace(microsecond=0)
	sub_table=create.get_sub(all_sub,meta,time)
	meta = ['Code','Sub time','Score','Lang']
	if Us_Pro is None:
		return render(request, 'reverse.html',{'session':session,'Lang':'c','problem':problem ,'contest':contest,'sub_all':sub_table,'fields':meta,'end':str(contest.end_time)[:16:],'Rank':get_rank(user.id,contest.id),'S_Rate':problem.s_rate})
	else:
		if Us_Pro.last_lang == 'c':
			session = Us_Pro.c_session_code
		elif Us_Pro.last_lang == 'c_cpp':
			session = Us_Pro.cpp_session_code
		elif Us_Pro.last_lang == 'java':
			session = Us_Pro.java_session_code
		elif Us_Pro.last_lang == 'python' :
			session = Us_Pro.py_session_code
		elif Us_Pro.last_lang == 'python3' :
			session = Us_Pro.py3_session_code
		return render(request, 'reverse.html',{'session':session,'Lang':Us_Pro.last_lang,'problem':problem ,'contest':contest,'sub_all':sub_table,'fields':meta,'end':str(contest.end_time)[:16:],'Rank':get_rank(user.id,contest.id),'Status':Us_Pro.status,'S_Rate':problem.s_rate})
	

def check(request,problem_name):
	problem = Problem.objects.get(p_name=problem_name)
	R_problem = Reverse.objects.get(Problem=problem)
	input_for = request.POST.get('input')
	command = subprocess.Popen ("python "+R_problem.code.name, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
	command.stdin.write (input_for)
	command.stdin.close ()
	ans = ''
	ans = getO(command,2)
	return HttpResponse(ans)
