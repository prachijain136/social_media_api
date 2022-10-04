from rest_framework import serializers
from .models import Post
from  comments.serializers import CommentSerializer
class PostSerializer(serializers.ModelSerializer):
    comments=CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['id','post_title' ,'post_content','post_date','comments','no_of_likes','no_of_dislikes']
