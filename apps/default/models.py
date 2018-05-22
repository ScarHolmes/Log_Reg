from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import bcrypt
from bcrypt import checkpw
import re

EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
	def isValidRegistration(self, userInfo, request):
		passFlag = True
		if not userInfo['first_name'].isalpha():
		    messages.warning(request, 'First name contains non-alpha character(s)')
		    passFlag = False
		if len(userInfo['first_name']) < 2:
		    messages.warning(request, 'First name is not long enough.')
		    passFlag = False
		if not userInfo['last_name'].isalpha():
		    messages.warning(request, 'Last name contains non-alpha character(s)')
		    passFlag = False
		if len(userInfo['last_name']) < 2:
		    messages.warning(request, 'Last name is not long enough.')
		    passFlag = False
		if not EMAIL_REGEX.match(userInfo['email']):
		    messages.warning(request, 'Email is not a valid email!')
		    passFlag = False
		if len(userInfo['password']) < 7:
		    messages.warning(request, 'Password is not long enough.')
		    passFlag = False
		if User.objects.filter(email = userInfo['email']):
			messages.error(request, "This email already exists in our database.")
			passFlag = False

		if passFlag == True:
			messages.success(request, "Success! Welcome, " + userInfo['first_name'] + "!")
			hashed = bcrypt.hashpw(userInfo['password'].encode(), bcrypt.gensalt())
			User.objects.create(first_name = userInfo['first_name'], last_name = userInfo['last_name'], email = userInfo['email'], password = hashed)
		return passFlag
	
	def val_user(self, userInfo, request):
		passFlag = True
		user = User.objects.get(email=userInfo['email'])
		
		if bcrypt.checkpw(userInfo['password'].encode(), user.password.encode()):
			messages.success(request, "Success! Welcome," + " " + user.first_name)
			print (user.first_name)
		else:
			messages.error(request, "This password is incorrect")
			passFlag = False

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
