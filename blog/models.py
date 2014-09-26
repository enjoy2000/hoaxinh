from django.db import models
from django.contrib.auth.models import User

# Blog model
class Blog(models.Model):
	user = models.ForeignKey(User) # Use user_id from django auth as foreign key
	title = models.CharField(max_length=200)
	content = models.TextField()
	pub_date = models.DateTimeField('date published')