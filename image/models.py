from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Image(models.Model) :
	user = models.ForeignKey(User)
	name = models.ImageField(upload_to='hoaxinh')
	pub_date = models.DateTimeField('date published')