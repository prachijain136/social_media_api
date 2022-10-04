from django.db import models

class Follower(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    follower=models.CharField(max_length=400)
    def __str__(self):
        return self.follower

