from __future__ import unicode_literals

from django.db import models
import bcrypt

class UserManager(models.Manager):
	def registerValidation(self, postData):
		results = {'status': True, 'errors': []}
		user = []
		if not postData ['name'] or len(postData ['name']) < 3:
			results['status'] = False
			results['errors'].append('Name must be at least 3 characters long.')
		if not postData ['user_name'] or len(postData ['user_name']) < 3:
			results['status'] = False
			results['errors'].append('Username must be at least 3 characters long.')
		if not postData ['pw'] or len(postData ['pw']) < 8 or postData['pw'] != postData['confirmpw']:
			results['status'] = False
			results['errors'].append('Please confirm password is at least 8 characters long and matches your confirmation.')
		if results['status'] == True:
			user = User.objects.filter(user_name = postData['user_name'])
		if len(user) != 0:
			results['status'] = False
			results['errors'].append('Username already exists. Please choose a different one, or Log In.')
		return results

	def createUser(self, postData):
		p_hash = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt())
		user = User.objects.create(name = postData['name'], user_name = postData['user_name'], password = postData['pw'])
		return user

	def loginValidation(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		user = User.objects.filter(user_name = postData['user_name'])
		if len(user) <=0:
			results['status'] = False
			results['errors'].append('Please try entering your username again.')
		elif len(postData['pw']) < 5 or postData['pw'] != user[0].password:
			results['status'] = False
			results['errors'].append('Password is incorrect. Please try again.')
		else:
			results['user'] = user[0]
		return results

class User(models.Model):
	name = models.CharField(max_length=20)
	user_name = models.CharField(max_length=30)
	password = models.CharField(max_length=20)
	created_at = models.DateTimeField(auto_now_add = True)	
	objects = UserManager()
