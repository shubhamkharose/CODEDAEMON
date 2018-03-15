from django.db import models
class User(models.Model):
	name=models.CharField(max_length=250)
	username=models.CharField(max_length=250)
	password=models.CharField(max_length=250)
	email=models.EmailField(max_length=250)
	contact=models.CharField(max_length=10)
	clgname=models.CharField(max_length=250)
	languages=models.CharField(max_length=250)
	experience=models.CharField(max_length=250)
	#dp=models.ImageField()

	def __str__(self):
	    return self.username

class AdminUser(models.Model):
	user = models.ForeignKey(User,on_delete= models.CASCADE)
