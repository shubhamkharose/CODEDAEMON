from django.db import models
from login.models import User
# Create your models here.
class Contest(models.Model):
	con_name=models.CharField(max_length=250)
	con_date=models.DateField(blank=True)
	start_time=models.DateTimeField(blank=True)
	start = models.CharField(max_length=100)
	end_time=models.DateTimeField(blank=True)
	end = models.CharField(max_length=100)
	org_name=models.CharField(max_length=250)
	image=models.CharField(max_length=250)
	tagline=models.CharField(max_length=250)
	disc=models.TextField()
	rules=models.TextField()
	prize=models.TextField()
	scoring=models.TextField()

	def __str__(self):
	    return "Contest Name : %s Contest id %d" % (self.con_name,self.id)

class Problem(models.Model):
	Contest=models.ForeignKey(Contest,on_delete=models.CASCADE)
	p_name=models.CharField(max_length=250)	#name
	r_flag=models.BooleanField(default=False)
	p_level=models.CharField(max_length=250)
	p_disc=models.TextField() # description
	p_input=models.TextField() # input Format
	p_cons=models.TextField() # constraints
	p_output=models.TextField() # o/p format
	sample_input=models.TextField() 
	sample_output=models.TextField()
	exp=models.TextField() #explanations
	# From Compile_run

	success_sub = models.IntegerField(default=0) # for suces rate
	tot_sub = models.IntegerField(default=0)
	score = models.IntegerField() #Total score
	s_rate = models.CharField(max_length=6)

	def __str__(self):
		if(self.tot_sub == 0):
		    return "Problem Id : %d -- %s - Success Rate : %.2f - Score : %d" % (self.id,self.p_name,0,self.score)
		else:
		    return "Problem Id : %d -- %s - Success Rate : %.2f - Score : %d" % (self.id,self.p_name , (((self.success_sub*1.0) / self.tot_sub)*100),self.score)


class Con_signup(models.Model):
	contest=models.ForeignKey(Contest,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	status=models.BooleanField(default=False)
	def __str__(self):
		return self.contest.con_name + " "+self.user.username

		
class Contact(models.Model):
	name=models.CharField(max_length=250)
	email=models.CharField(max_length=250)
	sub=models.CharField(max_length=250)
	message=models.CharField(max_length=250)
