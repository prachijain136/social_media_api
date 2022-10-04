from django.db import models
# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    post_title=models.CharField(max_length=100)
    post_content=models.CharField(max_length=4000)
    post_date=models.DateField(auto_now_add=True)
    no_of_likes = models.IntegerField(default=0)
    no_of_dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.post_title