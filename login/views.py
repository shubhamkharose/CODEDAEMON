from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import User
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required 
from django.core.mail import send_mail,EmailMessage
from django.core.urlresolvers import reverse
from django.core.mail import send_mail,EmailMessage
from Compile_run.views import createfolders

from home.views import get_u


def index(request):
	msg=''
	return render(request,'login/index.html',{'msg':msg})

def validate(username):
	if username.find(".")>0 or username.find("\\")>0  or username.find('/')>0 or username.find(':')>0  or username.find('*')>0  or username.find('?')>0  or username.find('\"')>0  or username.find('\'')>0  or username.find('<')>0  or username.find('>')>0  or username.find('|')>0  or username.find('.')>0 :
		return False
	tmp=User.objects.filter(username=username).first()
	if tmp is not None:
		return False
	return True

def signup(request):
	if request.method=='POST':
		print("In Signup")
		username=request.POST.get('username')
		if validate(username):
			form=User(name=request.POST.get('name'),username=username,password=request.POST.get('pwd'),email=request.POST.get('email'),contact=request.POST.get('contact'))
			form.save()
			createfolders(username)
			msg='success'
			return HttpResponse(msg)
		print username , " -- tried by -- ", request.POST.get('name') ,' & ', request.POST.get('email')
		msg='not'
				
		return HttpResponse(msg)

def signin(request):
	if request.method == 'POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		users=User.objects.filter(username=username,password=password)
		request.session['user']=username
		if users.__len__()==1:
			return HttpResponse("success")
		else:
			return HttpResponse("Invalid login..!!")

def forgot(request):
	email=request.POST.get('email')
	users=User.objects.filter(email=email)
	users2=get_object_or_404(User,email=email)
	if users.__len__()==1:
		send_mail('Password',"Your existing password is:"+users2.password,'programtowin@gmail.com',[email],fail_silently=False,)
	msg=''
	return render(request,'login/index.html',{'msg':msg})
