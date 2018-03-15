from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import User_Problem,TestCase,Problem_session,AdminSettings
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
from home.views import get_u


idealbuffer = 1

def index(request,problem_name):
	problem = Problem.objects.get(p_name=problem_name)
	#try:
	#	s_rate = (((problem.success_sub*1.0) / problem.tot_sub)*100)
	#except :
	#	s_rate = 0
	#s_rate = (str)(round(s_rate,2))
	

	contest =problem.Contest
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
		return render(request, 'submission/Drop.html',{'session':session,'Lang':'c','problem':problem ,'contest':contest,'sub_all':sub_table,'fields':meta,'end':str(contest.end_time)[:16:],'Rank':get_rank(user.id,contest.id),'S_Rate':problem.s_rate})
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
		return render(request, 'submission/Drop.html',{'session':session,'Lang':Us_Pro.last_lang,'problem':problem ,'contest':contest,'sub_all':sub_table,'fields':meta,'end':str(contest.end_time)[:16:],'Rank':get_rank(user.id,contest.id),'Status':Us_Pro.status,'S_Rate':problem.s_rate})

def safe_escape(ans):
	try:
		ans = escape(ans)
	except Exception:
		ans = '-{ truncated }--Provide neat input'
	return ans

def get_rank(user,contest_id):
	cont=apps.get_model(app_label='Leader', model_name="cont_"+str(contest_id))
	me = cont.objects.get(user=User.objects.get(id=user))
	all_users  = cont.objects.all()
	for rank,u in enumerate(all_users):
		if u == me:
			return rank+1

def deletefromtree(command,user):
	all_info,err = subprocess.Popen('ps --forest -o pid,cmd -g $(ps -o sid= -p '+str(command.pid)+')',shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT).communicate()
	rows = all_info.split("\n")
	print user.username
	time_out = False
	for i in rows:
		row = i.strip(' ')
		at = row.find('All/'+user.username)
		if at > 0 :
			pid = row.split(" ")[0]
			subprocess.Popen('kill '+pid,shell=True).communicate()
			print pid , 'killed from server'
			time_out=True
	return time_out

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

def getO(command,timeout,user):	
	poll_obj = select.poll()
	poll_obj.register(command.stdout, select.POLLIN)
	buflimit = AdminSettings.objects.get(id=1).buff
	buf = 0
	ans =''
	start = time.time()

	while buf <= buflimit and start + timeout > time.time() : 
		poll_result = poll_obj.poll(0)
		if poll_result:
			ans+= command.stdout.read(idealbuffer)
			buf+=idealbuffer
	
	return getWelO(ans),deletefromtree(command,user)


def createfolders(name):
	p = subprocess.Popen('mkdir All/'+name,shell=True)
	p.communicate()
	p = subprocess.Popen('mkdir All/'+name+'/c',shell=True)
	p.communicate()
	p = subprocess.Popen('mkdir All/'+name+'/cpp',shell=True)
	p.communicate()
	p = subprocess.Popen('mkdir All/'+name+'/java',shell=True)
	p.communicate()
	p = subprocess.Popen('mkdir All/'+name+'/py',shell=True)
	p.communicate()
	p = subprocess.Popen('mkdir All/'+name+'/py3',shell=True)
	p.communicate()
	
def pushindb(user,problem,points,Lang,code,result):
	contest_leader=apps.get_model(app_label='Leader', model_name="cont_"+str(problem.Contest.id))
	Submission=apps.get_model(app_label='Leader', model_name="Sub_cont_"+str(problem.Contest.id))
	Us_Pro = User_Problem.objects.filter(User=user, Problem=problem).first()
	row = contest_leader.objects.get(user=user)
	tmp_score = getattr(row,problem.p_name)				
	now_time = datetime.datetime.now ()
	if tmp_score < points and now_time <= problem.Contest.end_time:
		tot = getattr(row,"tot_score")
		tot -= tmp_score
		tot += points
		setattr(row,"tot_score",tot)
		setattr(row,problem.p_name,points)
		setattr(row,"sub_time",datetime.datetime.now())
		Us_Pro.score = points
		row.save()
		if (problem.score == points):
			Us_Pro.status = True
			problem.success_sub += 1

	Us_Pro.save()
	Sub = Submission (User=user, Problem=problem, Lang=Lang, code=code, pts=points, res=result,time=str (now_time))
	Sub.save ()
	try:
		s_rate = (((problem.success_sub*1.0) / problem.tot_sub)*100)
	except:
		s_rate = 0
	s_rate = (str)(round(s_rate,2))
	problem.s_rate = s_rate
	problem.save()
	#print 'Obk=ject Saved',problem.tot_sub

def change(request,problem_id):
	if request.method == 'POST':
		user = get_u(request)
		user = get_object_or_404 (User,username=user)
		problem = get_object_or_404(Problem,id=problem_id)
		Us_Pro = User_Problem.objects.filter(User=user, Problem=problem).first()
		#print (Us_Pro)
		Lang = request.POST.get('lang')
		if Lang == 'c':
			if Us_Pro is None or Us_Pro.c_session_code is None :
				session = Problem_session.objects.get(Problem=problem)
				return HttpResponse(session.c_session_code)
			return HttpResponse(Us_Pro.c_session_code)
		elif Lang == 'c_cpp':
			if Us_Pro is None or Us_Pro.cpp_session_code is None:
				session = Problem_session.objects.get(Problem=problem)
				return HttpResponse(session.cpp_session_code)
			return HttpResponse(Us_Pro.cpp_session_code)
		elif Lang == 'java':
			if Us_Pro is None or Us_Pro.java_session_code is None:
				session = Problem_session.objects.get(Problem=problem)
				return HttpResponse(session.java_session_code)
			return HttpResponse(Us_Pro.java_session_code)
		elif Lang == 'python' :
			if Us_Pro is None or Us_Pro.py_session_code is None:
				session = Problem_session.objects.get(Problem=problem)
				return HttpResponse(session.py_session_code)
			return HttpResponse(Us_Pro.py_session_code)
		elif Lang == 'python3' :
			if Us_Pro is None or Us_Pro.py3_session_code is None:
				session = Problem_session.objects.get(Problem=problem)
				return HttpResponse(session.py3_session_code)
			return HttpResponse(Us_Pro.py3_session_code)


def code(request,problem_id,sub_id):
	
	problem = get_object_or_404(Problem,id=problem_id)
	Submission=apps.get_model(app_label='Leader', model_name="Sub_cont_"+str(problem.Contest.id))
	if get_object_or_404(Submission,id=sub_id).User.username == request.session['user']:
		return render(request,'submission/code.html',{'code':Submission.objects.get(id=sub_id).code})
	else:
		return HttpResponse("No Access !")

def submit(request,problem_id):
	if request.method == 'POST':
		time_out=False
		user = get_u(request)
		code = request.POST.get('code')
		Lang = request.POST.get('lang')
		errors = ''
		
		user = get_object_or_404 (User,username=user)
		problem = get_object_or_404(Problem,id=problem_id)
		#print (problem)
		#code = code.replace ('\n', '')

		Us_Pro = User_Problem.objects.filter(User=user, Problem=problem).first()
		

		if Us_Pro is None :
			Us_Pro = User_Problem(User=user,Problem=problem,sub_cnt=0)
			problem.tot_sub = problem.tot_sub + 1
			problem.save()
			Us_Pro.save()

		if Lang == 'c':
			#Us_Pro = User_Problem.objects.get (User=user, Problem=problem)
			cnt = Us_Pro.sub_cnt

			
			Us_Pro.c_session_code = code
			Us_Pro.last_lang ='c'
			Us_Pro.save ()
			points = 0
			result = ''

			file_name = 'All/'+user.username+'/c/Solution.c'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			command = subprocess.Popen ('gcc All/'+user.username+'/c/Solution.c -o All/'+user.username+"/c/"+user.username, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

			ans,err = command.communicate()
			subprocess.Popen('kill '+str(command.pid),shell=True)
	
			           #py 3.4 
			#ans += x               django 1.11 py 2.7/ 3.4
			if (len (ans) > 1):
				return HttpResponse(safe_escape(ans))
			else:
				test_case = 1
				for test0 in TestCase.objects.filter (Problem=problem):
					ans = ''
					#print ('test')
					##print(test0)
					command = subprocess.Popen ("./All/"+user.username+"/c/"+user.username, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
					#print ("testing .out created")
					command.stdin.write (test0.testin)
					command.stdin.close ()
					timeout = AdminSettings.objects.get(id=1).c_time
					ans,time_out = getO(command,timeout,user)
					if time_out:
						result +="TLE\t\t"
						if test_case % 4 == 0:
							result += '\n\n'
					elif (ans == test0.testout):
						result += 'TestCase ' + str (test_case) + ' <i class=\"green checkmark icon\"></i>\t\t'
						if test_case % 4 == 0:
							result += '\n\n'
						points += test0.weight
					else:
						result += 'TestCase ' + str (test_case) + '  <i class=\"red remove icon\"></i>\t\t' 
						if test_case % 4 == 0:
							result += '\n\n'
					test_case+=1
				pushindb(user,problem,points,Lang,code,result)
				return HttpResponse("<pre><strong>"+result+"</strong></pre>")
		elif Lang == 'c_cpp':
			#Us_Pro = User_Problem.objects.get (User=user, Problem=problem)
			cnt = Us_Pro.sub_cnt
			Us_Pro.sub_cnt += 1
			Us_Pro.last_lang ='c_cpp'
			Us_Pro.cpp_session_code = code
			Us_Pro.save ()
			points = 0
			result = ''

			file_name = 'All/'+user.username+'/cpp/Solution.cpp'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			command = subprocess.Popen ('g++ All/'+user.username+'/cpp/Solution.cpp -o All/'+user.username+"//cpp/"+user.username, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

			ans,err = command.communicate()
			subprocess.Popen('kill '+str(command.pid),shell=True)
	           #py 3.4 
			#ans += x               django 1.11 py 2.7/ 3.4
			if (len (ans) > 1):
				return HttpResponse(safe_escape(ans))
			else:
				test_case = 1
				for test0 in TestCase.objects.filter (Problem=problem):
					ans = ''
					print ('test0',len(test0.testin))
					##print(test0)
					command = subprocess.Popen ("./All/"+user.username+"/cpp/"+user.username, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
					#print ("testing .out created")
					command.stdin.write (test0.testin)
					command.stdin.close ()
					timeout = AdminSettings.objects.get(id=1).cpp_time
					ans,time_out = getO(command,timeout,user)
					if time_out:
						result +="TLE\t\t"
						if test_case % 4 == 0:
							result += '\n\n'
					elif (ans == test0.testout):
						result += 'TestCase ' + str (test_case) + ' <i class=\"green checkmark icon\"></i>\t\t'
						if test_case % 4 == 0:
							result += '\n\n'
						points += test0.weight
					else:
						result += 'TestCase ' + str (test_case) + '  <i class=\"red remove icon\"></i>\t\t' 
						if test_case % 4 == 0:
							result += '\n\n'
						print len(test0.testout) , len(ans)
					test_case+=1
				pushindb(user,problem,points,Lang,code,result)
				return HttpResponse("<pre><strong>"+result+"</strong></pre>")
		elif Lang == 'java':
			#Us_Pro = User_Problem.objects.get (User=user, Problem=problem)
			cnt = Us_Pro.sub_cnt
			Us_Pro.sub_cnt += 1
			Us_Pro.java_session_code = code
			Us_Pro.last_lang ='java'
			Us_Pro.save ()
			points = 0
			result = ''

			file_name = 'All/'+user.username+'/java/Solution.java'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			command = subprocess.Popen ('javac All/'+user.username+'/java/Solution.java ', shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

			ans,err = command.communicate()
			subprocess.Popen('kill '+str(command.pid),shell=True)
				
			print 'comm'         #py 3.4 
			#ans += x               django 1.11 py 2.7/ 3.4
			if (len (ans) > 1):
				return HttpResponse(safe_escape(ans))
			else:
				test_case = 1
				for test0 in TestCase.objects.filter (Problem=problem):
					ans = ''
					#print ('test')
					##print(test0)
					command = subprocess.Popen ("java -cp All/"+user.username+"/java/ Solution", shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
					#print ("testing .out created")
					command.stdin.write (test0.testin)
					command.stdin.close ()
					timeout = AdminSettings.objects.get(id=1).java_time
					ans,time_out = getO(command,timeout,user)
					if time_out:
						result +="TLE\t\t"
						if test_case % 4 == 0:
							result += '\n\n'
					elif (ans == test0.testout):
						result += 'TestCase ' + str (test_case) + ' <i class=\"green checkmark icon\"></i>\t\t'
						if test_case % 4 == 0:
							result += '\n\n'
						points += test0.weight
					else:
						result += 'TestCase ' + str (test_case) + '  <i class=\"red remove icon\"></i>\t\t' 
						if test_case % 4 == 0:
							result += '\n\n'
					test_case+=1
				pushindb(user,problem,points,Lang,code,result)
				return HttpResponse("<pre><strong>"+result+"</strong></pre>")
		elif Lang == 'python':
			#Us_Pro = User_Problem.objects.get (User=user, Problem=problem)
			cnt = Us_Pro.sub_cnt
			Us_Pro.sub_cnt += 1
			Us_Pro.py_session_code = code
			Us_Pro.last_lang ='python'
			Us_Pro.save ()
			points = 0
			result = ''

			file_name = 'All/'+user.username+'/py/Solution.py'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			test_case = 1
			for test0 in TestCase.objects.filter (Problem=problem):
				ans = ''
				#print ('test')
				##print(test0)
				command = subprocess.Popen ('python All/'+user.username+'/py/Solution.py', shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
				#print ("testing .out created")
				command.stdin.write (test0.testin)
				command.stdin.close ()
				timeout = AdminSettings.objects.get(id=1).py_time
				ans,time_out = getO(command,timeout,user)
				if time_out:
					result +="TLE\t\t"
					if test_case % 4 == 0:
						result += '\n\n'
				elif (ans == test0.testout):
					result += 'TestCase ' + str (test_case) + ' <i class=\"green checkmark icon\"></i>\t\t'
					if test_case % 4 == 0:
						result += '\n\n'
					points += test0.weight
				else:
					result += 'TestCase ' + str (test_case) + '  <i class=\"red remove icon\"></i>\t\t' 
					if test_case % 4 == 0:
						result += '\n\n'
				test_case+=1
			pushindb(user,problem,points,Lang,code,result)
			return HttpResponse("<pre><strong>"+result+"</strong></pre>")
		elif Lang == 'python3':
			#Us_Pro = User_Problem.objects.get (User=user, Problem=problem)
			cnt = Us_Pro.sub_cnt
			Us_Pro.sub_cnt += 1
			Us_Pro.last_lang ='python3'
			Us_Pro.py3_session_code = code
			Us_Pro.save ()
			points = 0
			result = ''

			file_name = 'All/'+user.username+'/py3/Solution.py'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			test_case = 1
			for test0 in TestCase.objects.filter (Problem=problem):
				ans = ''
				#print ('test')
				#print(test0)
				command = subprocess.Popen ('python3 All/'+user.username+'/py3/Solution.py', shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
				#print ("testing .out created")
				command.stdin.write (test0.testin)
				command.stdin.close ()
				timeout = AdminSettings.objects.get(id=1).py3_time
				ans,time_out = getO(command,timeout,user)
				if time_out:
					result +="TLE\t\t"
					if test_case % 4 == 0:
						result += '\n\n'
				elif (ans == test0.testout):				
					result += 'TestCase ' + str (test_case) + ' <i class=\"green checkmark icon\"></i>\t\t'
					if test_case % 4 == 0:
						result += '\n\n'
					points += test0.weight
				else:
					result += 'TestCase ' + str (test_case) + '  <i class=\"red remove icon\"></i>\t\t' 
					if test_case % 4 == 0:
						result += '\n\n'
				test_case+=1
			pushindb(user,problem,points,Lang,code,result)

			return HttpResponse("<pre><strong>"+result+"</strong></pre>")


def run(request,problem_id):
	if request.method == 'POST':
		time_out=False
		user = get_u(request)
		code = request.POST.get('code')
		Lang = request.POST.get('lang')
		status = request.POST.get('Check_Status')
		
		errors = ''
		
		user = get_object_or_404 (User,username=user)
		problem = get_object_or_404(Problem,id=problem_id)
		#print status,"-------"
		if status == "yes" :
			input_from_user = request.POST.get('input')
		else:
			input_from_user = problem.sample_input
			
		#print (problem)
		Us_Pro = User_Problem.objects.filter(User=user, Problem=problem).first()
		#print (Us_Pro)

		if Us_Pro is None :
			Us_Pro = User_Problem(User=user,Problem=problem,sub_cnt=0)
			problem.tot_sub+=1
			problem.save()
			Us_Pro.save()

		if Lang == 'c':
			Us_Pro.c_session_code = code
			Us_Pro.last_lang ='c'
			Us_Pro.save ()

			file_name = 'All/'+user.username+'/c/Solution.c'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			command = subprocess.Popen ('gcc All/'+user.username+'/c/Solution.c -o All/'+user.username+"/c/"+user.username, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

			ans,err = command.communicate()
			subprocess.Popen('kill '+str(command.pid),shell=True)
	          #py 3.4 
			#ans += x               django 1.11 py 2.7/ 3.4
			if (len (ans) > 1):
				return  HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre>")
			else:
				ans = ''
				#print ('test')
				
				command = subprocess.Popen ("./All/"+user.username+"/c/"+user.username, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
				#print ("testing .out created")
				command.stdin.write (input_from_user)
				command.stdin.close ()
				timeout = AdminSettings.objects.get(id=1).c_time
				ans,time_out = getO(command,timeout,user)
			if time_out:
				return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">"+"Terminate due to timeout"+"\n\n\nYour Output : \n"+safe_escape(ans)+"</pre>")
			if status == "yes":
				return HttpResponse(safe_escape(ans))
			else:
				if problem.sample_output == ans :
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre><p><strong class=\"header\">Result :</strong></p>"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">You passed sample testcase</strong></pre>")
				else:
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre><p><strong class=\"header\">Result :</strong></p>"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">Wrong output</strong></pre>")
			
			
		elif Lang == 'c_cpp':
			Us_Pro.cpp_session_code = code
			Us_Pro.last_lang ='c_cpp'
			Us_Pro.save ()

			file_name = 'All/'+user.username+'/cpp/Solution.cpp'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			command = subprocess.Popen ('g++ All/'+user.username+'/cpp/Solution.cpp -o All/'+user.username+"//cpp/"+user.username, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

			ans,err = command.communicate()
			subprocess.Popen('kill '+str(command.pid),shell=True)
	           #py 3.4 
			#ans += x               django 1.11 py 2.7/ 3.4
			if (len (ans) > 1):
				
				return  HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre>")
			else:
				ans = ''
				command = subprocess.Popen ("./All/"+user.username+"/cpp/"+user.username, shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
				#print ("testing .out created")
				command.stdin.write (input_from_user)
				command.stdin.close ()
				timeout = AdminSettings.objects.get(id=1).cpp_time
				ans,time_out = getO(command,timeout,user)
			if time_out:
				return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">"+"Terminate due to timeout"+"\n\n\nYour Output : \n"+safe_escape(ans)+"</pre>")
			if status == "yes" :
				return HttpResponse(safe_escape(ans))
			else:
				if problem.sample_output == ans :
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">"+safe_escape(ans)+"</strong></pre><br>Result :"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">You passed sample testcase</strong></pre>")
				else:
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">"+safe_escape(ans)+"</strong></pre><br>Result :"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">Wrong output</strong></pre>")
			
					
		elif Lang == 'java':
			Us_Pro.java_session_code = code
			Us_Pro.last_lang ='java'
			Us_Pro.save ()
			
			file_name = 'All/'+user.username+'/java/Solution.java'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			command = subprocess.Popen ('javac All/'+user.username+'/java/Solution.java ', shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT)

			ans,err = command.communicate()
			subprocess.Popen('kill '+str(command.pid),shell=True)
	         #py 3.4 
			#ans += x               django 1.11 py 2.7/ 3.4
			if (len (ans) > 1):
				
				return  HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre>")
			else:
				ans = ''
				command = subprocess.Popen ("java -cp All/"+user.username+"/java/ Solution", shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
				#print ("testing .out created")
				command.stdin.write (input_from_user)
				command.stdin.close ()
				time.sleep(.1)
				timeout = AdminSettings.objects.get(id=1).java_time
				ans,time_out = getO(command,timeout,user)
				
			if time_out:
				return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">"+"Terminate due to timeout"+"\n\n\nYour Output : \n"+safe_escape(ans)+"</pre>")	

			if status == "yes" :
				return HttpResponse(safe_escape(ans))
			else:
				if problem.sample_output == ans :
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre><p><strong class=\"header\">Result :</strong></p>"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">You passed sample testcase</strong></pre>")
				else:
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre><p><strong class=\"header\">Result :</strong></p>"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">Wrong output</strong></pre>")
			

		elif Lang == 'python':
			
			Us_Pro.py_session_code = code
			Us_Pro.last_lang ='python'
			Us_Pro.save ()
			
			file_name = 'All/'+user.username+'/py/Solution.py'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			command = subprocess.Popen ('python All/'+user.username+'/py/Solution.py', shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
			#print ("testing .out created")
			command.stdin.write (input_from_user)
			command.stdin.close ()
			timeout = AdminSettings.objects.get(id=1).py_time
			ans,time_out = getO(command,timeout,user)
			if time_out:
				return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">"+"Terminate due to timeout"+"\n\n\nYour Output : \n"+safe_escape(ans)+"</pre>")
			if status == "yes" :
				return HttpResponse(safe_escape(ans))
			else:
				if problem.sample_output == ans :
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">"+escape(ans)+"</strong></pre><br>Result :"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">You passed sample testcase</strong></pre>")
				else:
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre><p><strong class=\"header\">Result :</strong></p>"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">Wrong output</strong></pre>")
		elif Lang == 'python3':
			
			Us_Pro.py3_session_code = code
			Us_Pro.last_lang ='python3'
			Us_Pro.save ()
			
			file_name = 'All/'+user.username+'/py3/Solution.py'
			file = open (file_name, 'w')
			file.write (code)
			file.close ()
			#print ('File created')
			ans = ''
			command = subprocess.Popen ('python3 All/'+user.username+'/py3/Solution.py', shell=True, stdout=subprocess.PIPE,stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
			#print ("testing .out created")
			command.stdin.write (input_from_user)
			command.stdin.close ()
			time.sleep(1)
			timeout = AdminSettings.objects.get(id=1).py3_time
			ans,time_out = getO(command,timeout,user)
			if time_out:
				return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">"+"Terminate due to timeout"+"\n\n\nYour Output : \n"+safe_escape(ans)+"</pre>")
			if status == "yes" :
				return HttpResponse(safe_escape(ans))
			else:
				if problem.sample_output == ans :
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre><p><strong class=\"header\">Result :</strong></p>"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">You passed sample testcase</strong></pre>")
				else:
					return HttpResponse("<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">" + safe_escape(ans) + "</pre><p><strong class=\"header\">Result :</strong></p>"+"<pre class=\"ui segment\" style=\"background-color: #f8f8f8;border:0px;\">Wrong output</strong></pre>")
		




