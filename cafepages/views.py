from django.shortcuts import render
from .forms import SignupForm
from django.contrib import messages
# Create your views here.
def index(request):
	context={}
	return render(request,'index.html',context)

def Dashboard(request):
	context={}
	return render(request,'dashboard.html',context)
def signup(request):
	form=SignupForm()
	if request.method=="POST":
		form=SignupForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.cleaned_data.get('username')
			messages.success(request,'Welcome!'+user)
			return redirect('index')
	context={'form':form}
	return render(request,'signup.html',context)