from django.shortcuts import render,redirect,get_list_or_404, get_object_or_404
from .forms import SignupForm,UserdetailModel,contactModelform
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings 
from django.contrib.auth import authenticate,logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.template.loader import render_to_string

# --------------------------------------------------------------------------------
def index(request):
	form=contactModelform()
	if request.method=='POST':

		print(request.POST)
		form=contactModelform(request.POST)
		if form.is_valid():
			form.save()
			fname=form.cleaned_data.get('fname')
			lname=form.cleaned_data.get('lname')
			return render(request,'index.html',{'fname':fname,'lname':lname})
			#messages.info(request, 'Thanks!'+fname+' '+lname+' '+'Your Querry is registered, We will get back to you soon!!' )
			# form=contactModelform()
	context={'form':form}
	return render(request,'index.html',context)
# --------------------------------------------------------------------------------
@login_required(login_url='/login')
def Dashboard(request):
	user=request.user
	# ide=user.id
	val=Userdetail.objects.filter(username=user)
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
			mail=form.cleaned_data.get('email')
			tempalte=render_to_string('email_template.html',{'name':user})
			email=EmailMessage(
			    'Subject here',
			    'Welcome!'+user+' Thanks for choosing us. We are top class, number one..chauchak service provider. Thanks Aapka Apna Bhai Service Bhai :) ',
			    settings.EMAIL_HOST_USER,
			    [mail],
			    )
			email.fail_silently=False,
			email.send()
			
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
			user=request.user
			val=Userdetail.objects.filter(username=user)
			context={'val':val}
			return render(request,'dashboard.html',context)

		else:
			messages.info(request,'Username/Password Incorrect!!')

	context= {}
	return render(request,'login.html',context)
# --------------------------------------------------------------------------------
@login_required(login_url='/login')
def update(request):
	form=UserdetailModel()
	if request.method=="POST":
			user=request.user
			# print(user,user.id)
			try:
				obj=Userdetail.objects.get(username=user)
			except:
				obj=None
			if obj is not None:
				form=UserdetailModel(request.POST,instance=obj)
				print(request.POST)
				if form.is_valid():
					print(form.cleaned_data)	
					a=form.save()
					a.username=request.user
					a.save()
					return redirect('dashboard')
			else:
				form=UserdetailModel(request.POST)
				print(request.POST)
				if form.is_valid():
					print(request.POST)
					form.save()
					return redirect('dashboard')
	user=request.user
	ide=user.id
	val = Userdetail.objects.filter(username=request.user)
	context={'form':form,'val':val,'ide':ide}
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
@login_required(login_url='/login')
def password_change(request):
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			# print(form.cleaned_data)
			update_session_auth_hash(request, user)  # Important!
			messages.success(request, 'Your password was successfully updated!')
			logout(request)
			return redirect('login')
		else:
			messages.error(request, 'Please correct the error below.')
	else:
		form = PasswordChangeForm(request.user)
		return render(request, 'password_change_form.html', {'form': form})
# ---------------------------------------------------------------------------------
	

