from django.shortcuts import render, redirect, HttpResponse
from models import User
from django.contrib import messages

def index(request):
	return render(request, 'login_app/index.html')

def register(request):
	results = User.objects.registerValidation(request.POST)
	if results ['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
	else: 
		user = User.objects.createUser(request.POST)
		messages.success(request, 'User has been created. You may now log in.')
	return redirect('/')

def login(request):
	results = User.objects.loginValidation(request.POST)
	if results['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
		return redirect('/')
	request.session['name'] = results['user'].name
	request.session['user_name'] = results['user'].user_name
	request.session['id'] = results['user'].id
	return redirect('/travels')

def loggedOut(request):
	messages.success(request, 'You have been logged out.')
	return render(request, 'login_app/index.html')

