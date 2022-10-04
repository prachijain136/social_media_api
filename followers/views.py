from django.shortcuts import render
from .models import Follower
from users.permissions import IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers, viewsets,status,permissions
from user_profile.models import UserProfile
from rest_framework.response import Response

from .serializers import FollowerSerializer



# Create your views here.
class FollowViewSet(viewsets.ModelViewSet):
    queryset=Follower.objects.all()
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
                        
    def perform_create(self, serializer):
       

        user_instance=get_object_or_404(UserProfile,pk=self.request.data['follower'])
        print(user_instance.owner)
        print(user_instance.id)
        #already_follower=Follower.objects.filter(owner=self.request.user,follower=user_instance).exists()
        #if already_follower:
        if Follower.objects.filter(owner=self.request.user,follower=user_instance.id).exists():
            raise serializers.ValidationError({"message":"You have already followed"})
        else:
            user_instance.no_of_followers=user_instance.no_of_followers+1
            user_instance.save()
            serializer.save(owner=self.request.user)
    
    



    


