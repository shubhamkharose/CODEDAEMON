from django.db import models
from login.models import User
from home.models import Contest


class Discussion(models.Model):
	message=models.TextField(max_length=250)
	time=models.DateTimeField()
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	contest=models.ForeignKey(Contest,on_delete=models.CASCADE)

	def __str__(self):
		return 'User : '+self.user.username + ' - Time : '+ str(self.time) + ' Message : ' + self.message 


