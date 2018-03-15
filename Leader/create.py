from django.db import models
import subprocess

from django.db import connection
import sys
from django.shortcuts import render
from datetime import datetime, date, timedelta

def createmodel(name, no):
    str_name="\nclass "+name
    str_name=str_name+"(models.Model): \n" \
    "\t\tuser=models.ForeignKey(User,on_delete= models.CASCADE)\n" \
    "\t\tsub_time=models.DateTimeField(blank=True)\n" \
    "\t\ttot_score=models.IntegerField(default=0)\n"
    for i in no:
        str_name = str_name+"\t\t"+i.p_name +"=models.IntegerField(default=0)\n"
    str_name+='\n\t\tdef __str__(self):\n\t\t\
        return "User : "+ self.user.username'    
    str_name=str_name+"\n\n\t\tclass Meta:\n\t\t\tordering = ['-tot_score','sub_time']"
    str_name+='\n\n'
    str_name+='class  Sub_'+name+"(models.Model):\n\t\tUser = models.ForeignKey(User, on_delete = models.CASCADE)"
    str_name+='\n\t\tProblem = models.ForeignKey(Problem, on_delete = models.CASCADE)'
    str_name+='\n\t\tcode = models.TextField(null=True)'
    str_name+='\n\t\ttime = models.DateTimeField()'
    str_name+='\n\t\tLang = models.CharField(max_length=10)'
    str_name+='\n\t\tpts = models.IntegerField(default=0)'
    str_name+='\n\t\tres = models.CharField(max_length=100)'
    str_name+='\n\t\tdef __str__(self):\n\t\t\
        return "Sub id : "+ str(self.id) + " - Sub Lang : " + self.Lang + " - Time : " + str(self.time) + " - Points : "+str(self.pts) +" - Result : " + self.res'
    
    str_name+='\n\n\t\tclass Meta:\n\t\t\tordering = ["-time"]'

    obj=open('Leader/models.py','a')
    obj.write(str_name)
    obj.close()
    obj=open('Leader/admin.py','a')
    str_reg="\nfrom .models import "+name+" \nadmin.site.register("+name+")\n"
    str_reg+="\nfrom .models import Sub_"+name+" \nadmin.site.register(Sub_"+name+")\n"
    obj.write(str_reg)
    obj.close()
    subprocess.Popen('python manage.py makemigrations Leader',stderr=subprocess.STDOUT,stdout=subprocess.PIPE,shell=True)

    return str_name

def splitm(meta):
    a=[]
    for i in meta:
        j = str(i).split('.')
        a.append(j[2])
    return a

def get_table(cont,fields, time_temp):
    events=[]
    for user in cont:
        tmp=[]
        for val in fields:
            attr_temp = getattr(user, val)

            if val == 'sub_time':
                attr_temp = attr_temp.replace(microsecond = 0)
                attr_temp = attr_temp - time_temp
            tmp.append(attr_temp)
        events.append(tmp)
    return events

def get_sub(sub_all,fields,time):
	events=[]
	for sub in sub_all:
		tmp=[]
		for val in fields:
			attr_temp = getattr(sub, val)
			if val == 'time':
				attr_temp = attr_temp.replace(microsecond=0)
				attr_temp = attr_temp-time
			tmp.append(attr_temp)
		events.append(tmp)
	return events

