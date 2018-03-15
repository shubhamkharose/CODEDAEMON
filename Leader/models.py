from django.db import models
from login.models import User
from home.models import Problem,Contest


class cont_1(models.Model): 
		user=models.ForeignKey(User,on_delete= models.CASCADE)
		sub_time=models.DateTimeField(blank=True)
		tot_score=models.IntegerField(default=0)
		Magical_String=models.IntegerField(default=0)
		Scan_Me=models.IntegerField(default=0)
		Cousins=models.IntegerField(default=0)

		def __str__(self):
		        return "User : "+ self.user.username

		class Meta:
			ordering = ['-tot_score','sub_time']

class  Sub_cont_1(models.Model):
		User = models.ForeignKey(User, on_delete = models.CASCADE)
		Problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
		code = models.TextField(null=True)
		time = models.DateTimeField()
		Lang = models.CharField(max_length=10)
		pts = models.IntegerField(default=0)
		res = models.CharField(max_length=100)
		def __str__(self):
		        return "Sub id : "+ str(self.id) + " - Sub Lang : " + self.Lang + " - Time : " + str(self.time) + " - Points : "+str(self.pts) +" - Result : " + self.res

		class Meta:
			ordering = ["-time"]
class cont_2(models.Model): 
		user=models.ForeignKey(User,on_delete= models.CASCADE)
		sub_time=models.DateTimeField(blank=True)
		tot_score=models.IntegerField(default=0)
		Special_Episodes=models.IntegerField(default=0)
		Lucifer_and_Subsequences=models.IntegerField(default=0)

		def __str__(self):
		        return "User : "+ self.user.username

		class Meta:
			ordering = ['-tot_score','sub_time']

class  Sub_cont_2(models.Model):
		User = models.ForeignKey(User, on_delete = models.CASCADE)
		Problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
		code = models.TextField(null=True)
		time = models.DateTimeField()
		Lang = models.CharField(max_length=10)
		pts = models.IntegerField(default=0)
		res = models.CharField(max_length=100)
		def __str__(self):
		        return "Sub id : "+ str(self.id) + " - Sub Lang : " + self.Lang + " - Time : " + str(self.time) + " - Points : "+str(self.pts) +" - Result : " + self.res

		class Meta:
			ordering = ["-time"]
class cont_3(models.Model): 
		user=models.ForeignKey(User,on_delete= models.CASCADE)
		sub_time=models.DateTimeField(blank=True)
		tot_score=models.IntegerField(default=0)
		Winter=models.IntegerField(default=0)
		Sum_Query=models.IntegerField(default=0)
		Array_Reverse=models.IntegerField(default=0)
		Code_Like_Nagini=models.IntegerField(default=0)

		def __str__(self):
		        return "User : "+ self.user.username

		class Meta:
			ordering = ['-tot_score','sub_time']

class  Sub_cont_3(models.Model):
		User = models.ForeignKey(User, on_delete = models.CASCADE)
		Problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
		code = models.TextField(null=True)
		time = models.DateTimeField()
		Lang = models.CharField(max_length=10)
		pts = models.IntegerField(default=0)
		res = models.CharField(max_length=100)
		def __str__(self):
		        return "Sub id : "+ str(self.id) + " - Sub Lang : " + self.Lang + " - Time : " + str(self.time) + " - Points : "+str(self.pts) +" - Result : " + self.res

		class Meta:
			ordering = ["-time"]


class cont_5(models.Model): 
		user=models.ForeignKey(User,on_delete= models.CASCADE)
		sub_time=models.DateTimeField(blank=True)
		tot_score=models.IntegerField(default=0)
		Goblins_and_hex=models.IntegerField(default=0)
		Branch_Change=models.IntegerField(default=0)
		Archers_on_Algebra=models.IntegerField(default=0)
		Builder_is_back=models.IntegerField(default=0)

		def __str__(self):
		        return "User : "+ self.user.username

		class Meta:
			ordering = ['-tot_score','sub_time']

class  Sub_cont_5(models.Model):
		User = models.ForeignKey(User, on_delete = models.CASCADE)
		Problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
		code = models.TextField(null=True)
		time = models.DateTimeField()
		Lang = models.CharField(max_length=10)
		pts = models.IntegerField(default=0)
		res = models.CharField(max_length=100)
		def __str__(self):
		        return "Sub id : "+ str(self.id) + " - Sub Lang : " + self.Lang + " - Time : " + str(self.time) + " - Points : "+str(self.pts) +" - Result : " + self.res

		class Meta:
			ordering = ["-time"]
class cont_6(models.Model): 
		user=models.ForeignKey(User,on_delete= models.CASCADE)
		sub_time=models.DateTimeField(blank=True)
		tot_score=models.IntegerField(default=0)
		Reverse_Coding_1=models.IntegerField(default=0)
		Reverse_Coding_2=models.IntegerField(default=0)
		Number_Conversion=models.IntegerField(default=0)
		Debug_Builder=models.IntegerField(default=0)

		def __str__(self):
		        return "User : "+ self.user.username

		class Meta:
			ordering = ['-tot_score','sub_time']

class  Sub_cont_6(models.Model):
		User = models.ForeignKey(User, on_delete = models.CASCADE)
		Problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
		code = models.TextField(null=True)
		time = models.DateTimeField()
		Lang = models.CharField(max_length=10)
		pts = models.IntegerField(default=0)
		res = models.CharField(max_length=100)
		def __str__(self):
		        return "Sub id : "+ str(self.id) + " - Sub Lang : " + self.Lang + " - Time : " + str(self.time) + " - Points : "+str(self.pts) +" - Result : " + self.res

		class Meta:
			ordering = ["-time"]
class cont_7(models.Model): 
		user=models.ForeignKey(User,on_delete= models.CASCADE)
		sub_time=models.DateTimeField(blank=True)
		tot_score=models.IntegerField(default=0)
		Barbarian_at_ATM=models.IntegerField(default=0)
		Builders_at_construction_site=models.IntegerField(default=0)
		Calculate_Triangles=models.IntegerField(default=0)
		Cool_And_JD=models.IntegerField(default=0)
		Pekka_in_Maze=models.IntegerField(default=0)

		def __str__(self):
		        return "User : "+ self.user.username

		class Meta:
			ordering = ['-tot_score','sub_time']

class  Sub_cont_7(models.Model):
		User = models.ForeignKey(User, on_delete = models.CASCADE)
		Problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
		code = models.TextField(null=True)
		time = models.DateTimeField()
		Lang = models.CharField(max_length=10)
		pts = models.IntegerField(default=0)
		res = models.CharField(max_length=100)
		def __str__(self):
		        return "Sub id : "+ str(self.id) + " - Sub Lang : " + self.Lang + " - Time : " + str(self.time) + " - Points : "+str(self.pts) +" - Result : " + self.res

		class Meta:
			ordering = ["-time"]
class cont_8(models.Model): 
		user=models.ForeignKey(User,on_delete= models.CASCADE)
		sub_time=models.DateTimeField(blank=True)
		tot_score=models.IntegerField(default=0)
		Build_the_Hut=models.IntegerField(default=0)
		Baby_Dragon=models.IntegerField(default=0)
		Dragon_and_reverse_coding=models.IntegerField(default=0)
		Giant_and_Dice=models.IntegerField(default=0)

		def __str__(self):
		        return "User : "+ self.user.username

		class Meta:
			ordering = ['-tot_score','sub_time']

class  Sub_cont_8(models.Model):
		User = models.ForeignKey(User, on_delete = models.CASCADE)
		Problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
		code = models.TextField(null=True)
		time = models.DateTimeField()
		Lang = models.CharField(max_length=10)
		pts = models.IntegerField(default=0)
		res = models.CharField(max_length=100)
		def __str__(self):
		        return "Sub id : "+ str(self.id) + " - Sub Lang : " + self.Lang + " - Time : " + str(self.time) + " - Points : "+str(self.pts) +" - Result : " + self.res

		class Meta:
			ordering = ["-time"]
class cont_9(models.Model): 
		user=models.ForeignKey(User,on_delete= models.CASCADE)
		sub_time=models.DateTimeField(blank=True)
		tot_score=models.IntegerField(default=0)
		Witch_And_Triangles=models.IntegerField(default=0)
		Bits_Magic_Cool=models.IntegerField(default=0)
		Mr_Hog_rider=models.IntegerField(default=0)
		Giant_And_Dice=models.IntegerField(default=0)
		Wizard_And_Encryption=models.IntegerField(default=0)

		def __str__(self):
		        return "User : "+ self.user.username

		class Meta:
			ordering = ['-tot_score','sub_time']

class  Sub_cont_9(models.Model):
		User = models.ForeignKey(User, on_delete = models.CASCADE)
		Problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
		code = models.TextField(null=True)
		time = models.DateTimeField()
		Lang = models.CharField(max_length=10)
		pts = models.IntegerField(default=0)
		res = models.CharField(max_length=100)
		def __str__(self):
		        return "Sub id : "+ str(self.id) + " - Sub Lang : " + self.Lang + " - Time : " + str(self.time) + " - Points : "+str(self.pts) +" - Result : " + self.res

		class Meta:
			ordering = ["-time"]