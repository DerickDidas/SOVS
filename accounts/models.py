from django.db import models
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Tick(models.Model):
    username = AbstractUser.username
    president = models.BooleanField(default=False)
    mp = models.BooleanField(default=False)
