from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Zealicon(models.Model):
	user = models.ForeignKey(User)
	image = models.ImageField(upload_to='static/images/')
