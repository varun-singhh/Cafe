from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import*

class SignupForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email','password1','password2']
class UserdetailModel(forms.ModelForm):
	class Meta:
		model=Userdetail
		fields='__all__'
class contactModelform(forms.ModelForm):
	class Meta:
		model=contactform
		fields='__all__'

