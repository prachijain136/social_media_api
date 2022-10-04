from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile_data')
    no_of_followers=models.IntegerField(default=0)
