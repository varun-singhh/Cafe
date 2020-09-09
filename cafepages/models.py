from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userdetail(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	phone=models.CharField(max_length=10,null=False,blank=True)
	College=models.CharField(max_length=10,null=False,blank=True)
	hostel=models.CharField(max_length=10,null=False,blank=True)
	year=models.CharField(max_length=10,null=False,blank=True)
	roll=models.CharField(max_length=10,null=False,blank=True)