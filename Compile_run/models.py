from django.db import models
from home.models import Problem
from login.models import User 

# Create your models here.

class TestCase(models.Model):
    Problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    testin = models.TextField()
    testout = models.TextField()
    weight = models.IntegerField()

    def __str__(self):
        return str(self.id) + ' Problem Id : ' + str(self.Problem.p_name) + ' - Weight : ' + str(self.weight)

class Problem_session(models.Model):
    Problem = models.ForeignKey (Problem, on_delete=models.CASCADE)
    c_session_code = models.TextField(null=True)
    cpp_session_code = models.TextField(null=True)
    java_session_code = models.TextField(null=True)
    py_session_code = models.TextField(null=True)
    py3_session_code = models.TextField(null=True)
    
    def __str__(self):

        return 'Problem Id : ' + str(self.Problem.p_name )


class User_Problem(models.Model):
    Problem = models.ForeignKey (Problem, on_delete=models.CASCADE)
    User = models.ForeignKey (User, on_delete=models.CASCADE)
    sub_cnt = models.IntegerField()
    status = models.BooleanField(default=False)
    score= models.IntegerField(default=0)
    last_lang = models.CharField(max_length=10,default='c')
    c_session_code = models.TextField(null=True)
    cpp_session_code = models.TextField(null=True)
    java_session_code = models.TextField(null=True)
    py_session_code = models.TextField(null=True)
    py3_session_code = models.TextField(null=True)
    def __str__(self):
        return 'Problem Id : ' + str(self.Problem.id) + ' - Sub_Count : ' + str(self.sub_cnt)

class AdminSettings(models.Model):
    c_time =  models.IntegerField(default=2)
    cpp_time =  models.IntegerField(default=2)
    java_time =  models.IntegerField(default=5)
    py_time =  models.IntegerField(default=2)
    py3_time =  models.IntegerField(default=2)
    buff = models.IntegerField(default=1024*50)