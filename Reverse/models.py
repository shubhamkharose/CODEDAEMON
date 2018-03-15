# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from home.models import Contest,Problem
# Create your models here.
class Reverse(models.Model):
	Problem = models.ForeignKey(Problem,on_delete=models.CASCADE)
	code=models.FileField()
	