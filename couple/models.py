from django.db import models
from django.contrib.auth.models import User
# Couple model
class Couple(models.Model):
	male = models.ForeignKey(User, related_name = 'male', null = True)
	female = models.ForeignKey(User, related_name = 'female', null = True)
	started_date = models.DateTimeField(null = True)
	male_name = models.CharField(max_length = 100, null = True)
	female_name = models.CharField(max_length = 100, null = True)

# Story model
class Story(models.Model):
	couple = models.ForeignKey(Couple)
	content = models.TextField()
	pub_date = models.DateTimeField('date published')