from posts.models import Post
from post_reactions.permissions_like import hasSelfVotedOrReadOnly as like_permission
from post_reactions.permissions_dis import hasSelfVotedOrReadOnly as dislike_permission
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets,status,permissions
from . models import Like,Dislike
from . serializers import LikeSerializer,DislikeSerializer


# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):

    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,like_permission]
    def perform_create(self, serializer):
        post_instance=get_object_or_404(Post,pk=self.request.data['post_like'])
        already_up_voted=Like.objects.filter(post_like=post_instance,owner_like=self.request.user).exists()
        if already_up_voted:
            raise serializers.ValidationError({"message":"You have already liked this post"})
        else:
            
            post_instance.no_of_likes=post_instance.no_of_likes+1
            post_instance.save()
            serializer.save(owner_like=self.request.user,post_like=post_instance)
           

class DislikeViewSet(viewsets.ModelViewSet):
  
    queryset=Dislike.objects.all()
    serializer_class=DislikeSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,dislike_permission]
    def perform_create(self, serializer):
        post_instance=get_object_or_404(Post,pk=self.request.data['post_dislike'])
        already_up_voted=Dislike.objects.filter(post_dislike=post_instance,owner_dislike=self.request.user).exists()
        if already_up_voted:
            raise serializers.ValidationError({"message":"You have already liked this post"})
        else:
            post_instance.no_of_dislikes=post_instance.no_of_dislikes+1
            post_instance.save()
            serializer.save(owner_dislike=self.request.user,post_dislike=post_instance)
            



