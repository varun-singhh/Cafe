from django.shortcuts import render,redirect,get_list_or_404, get_object_or_404
from .forms import SignupForm,UserdetailModel
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *

# --------------------------------------------------------------------------------
def index(request):
	context={}
	return render(request,'index.html',context)
# --------------------------------------------------------------------------------
@login_required(login_url='/login')
def Dashboard(request):
	val = Userdetail.objects.all()
	context={'val':val}
	return render(request,'dashboard.html',context)
# --------------------------------------------------------------------------------
def signup(request):
	form=SignupForm()
	if request.method=="POST":
		form=SignupForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,user+'! You are Successfully Registered')
			return redirect('login')
	context= {}
	return render(request,'signup.html',context)
# --------------------------------------------------------------------------------
def login(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password1')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			auth_login(request, user)
			val = Userdetail.objects.all()
			context= {'val':val}
			return render(request,'dashboard.html',context)

		else:
			messages.info(request,'Username/Password Incorrect!!')

	context= {}
	return render(request,'login.html',context)
# --------------------------------------------------------------------------------
@login_required(login_url='/login')
def update(request):
	form=UserdetailModel()
	# print(form)
	if request.method=="POST":

			user=request.user
			# print(user,user.id)
			try:
				obj=Userdetail.objects.get(username=user)
			except:
				obj=None
			print(obj)
			if obj is not None:
				form=UserdetailModel(request.POST,instance=obj)
				if form.is_valid():
					#UserdetailModel.objects.get(pk=user).exists()
					#if form.username exist():
						a=form.save()
						a.username=request.user
						a.save()
						return redirect('dashboard')
			else:
				form=UserdetailModel(request.POST)
				if form.is_valid():
					form.save()
					return redirect('dashboard')


				# else:
				# 	form.save()
				# 	return redirect('dashboard')
	val = Userdetail.objects.all()
	context={'form':form,'val':val}
	return render(request,'update.html',context)
# --------------------------------------------------------------------------------
@login_required(login_url='/login')
def view(response):
	return render(response, "update.html", {})
# --------------------------------------------------------------------------------
def logoutuser(request):
	logout(request)
	return redirect('login')
# --------------------------------------------------------------------------------