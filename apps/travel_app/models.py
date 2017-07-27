from __future__ import unicode_literals

from django.db import models

from ..login_app.models import User
from datetime import date

class TripManager(models.Manager):
	def tripValidation(self, postData):
		results = {'status': True, 'errors': []}
		tripInstance = []
		if not postData ['destination'] or len(postData ['destination']) < 2:
			results['status'] = False
			results['errors'].append('Please re-enter destination name. Destination must be 2 or more characters long.')
		if not postData ['description'] or len(postData ['description']) < 10:
			results['status'] = False
			results['errors'].append('Please add a short description of your plans.')	 		
		return results

class Trip(models.Model):
	destination = models.CharField(max_length=30)
	description = models.CharField(max_length=150)
	date_from = models.DateField()
	date_to = models.DateField()
	coordinator = models.ForeignKey(User, default=1, null=True)
	traveler = models.ManyToManyField(User, default=1, related_name="traveler")
	objects = TripManager()


	