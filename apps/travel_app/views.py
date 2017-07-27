from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .. login_app.models import User
from models import Trip

def index(request):
	if not request.session['id']:
		return redirect('/')
	context = {
	"trips": Trip.objects.filter(coordinator = request.session['id']),
	"other_trips": Trip.objects.exclude(coordinator = request.session['id'])
	
	}
	print Trip.objects.filter(coordinator = request.session['id'])
	return render(request, 'travel_app/index.html', context)

def logout(request):
	request.session['id'] = None
	return redirect('/loggedOut')

def add(request):
	if not request.session['id']:
		return redirect('/')
	return render(request, 'travel_app/plan.html')

def addTrip(request):
	user = User.objects.get(id = request.session['id'])
	results = Trip.objects.tripValidation(request.POST)
	if results ['status'] == False:
		for error in results['errors']:
			messages.error(request, error)
	else: 
		tripInstance = Trip.objects.create(coordinator = user, destination = request.POST['destination'], description = request.POST['description'], date_from = request.POST['date_from'], date_to = request.POST['date_to'],)
	
	return redirect('/travels')

def delete(request, id):
	Trip.objects.get(id = id).delete()
	return redirect('/travels')

def destination(request, id):
	if not request.session['id']:
		return redirect('/')

	context = {
	"thisTrip": Trip.objects.get(id=id),
	
	"travelers": Trip.objects.exclude(coordinator = request.session['id']),
	}
	
	return render(request, 'travel_app/trip.html', context)

def join(request, id):
	trip = Trip.objects.get(id = id)
	user = User.objects.get(id=request.session['id'])

	x = trip.traveler.add(user)
	for x in trip.traveler.all():
		if x == user:
			break
		else:
			trip.traveler.add(user)
	
		print x.name 
	return redirect('/travels')


	
