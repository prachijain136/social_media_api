from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from users.permissions import IsOwnerOrReadOnly
from rest_framework import status, viewsets
from rest_framework import permissions
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)