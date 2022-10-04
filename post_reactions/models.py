from django.db import models
from posts.models import Post
# Create your models here.
class Like(models.Model):
    post_like=models.ForeignKey(Post,related_name='post_like',on_delete=models.CASCADE)
    owner_like = models.ForeignKey('auth.User', related_name='owner_like', on_delete=models.CASCADE)
    def __str__(self):
        return self.post_like.post_title


class Dislike(models.Model):
    post_dislike=models.ForeignKey(Post,related_name='post_dislike',on_delete=models.CASCADE)
    owner_dislike = models.ForeignKey('auth.User', related_name='owner_dislike', on_delete=models.CASCADE)
    def __str__(self):
        return self.post_dislike.post_title