from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Userdetail(models.Model):
	username = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	phone=models.CharField(max_length=10,null=False,blank=True)
	College=models.CharField(max_length=80,null=False,blank=True)
	hostel=models.CharField(max_length=10,null=False,blank=True)
	year=models.CharField(max_length=10,null=False,blank=True)
	roll=models.CharField(max_length=10,null=False,blank=True)
class contactform(models.Model):
	fname = models.CharField(max_length=20,null=False,blank=True)
	lname=models.CharField(max_length=20,null=False,blank=True)
	subject=models.CharField(max_length=100,null=False,blank=True)
	email=models.EmailField(max_length=50,null=False,blank=True)
	message=models.TextField(max_length=1000,null=False,blank=True)