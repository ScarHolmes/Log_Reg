
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse
def index(request):
    
    return render(request, "default/index.html")

def register(request):
	if request.method == "POST":
		passFlag = User.objects.isValidRegistration(request.POST, request)
		if passFlag == True:
			return redirect ('/')
		else:
			form = (request.POST)
			return redirect('/', {'form': form})
def login(request):
	if request.method == "POST":
		passFlag = User.objects.val_user(request.POST, request)
		if passFlag == True:
			return redirect ('/')
		else:
			form = (request.POST)
			return redirect('/', {'form': form})


# def show(request):
# 	context= {
# 	use = Users.objects.all()
# }
# return render(request, )


