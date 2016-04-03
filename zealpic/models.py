from django.db import models
from avatar.settings import MEDIA_URL

from django.contrib.auth.models import User
# Create your models here.
class Zealicon(models.Model):
	user = models.ForeignKey(User)
	image = models.ImageField(upload_to='images/')

