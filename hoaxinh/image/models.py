from django.db import models

# Create your models here.
class Image(models.Model) :
	name = models.ImageField(upload_to='hoaxinh')