
from django.shortcuts import render
from rest_framework import viewsets,status
from django.contrib.auth.models import User
from rest_framework.response import Response
from users.serializers import UserSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class UserViewSets(viewsets.ViewSet):
    def list(self,request):
        queryset=User.objects.all()
        serializer=UserSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self,request,pk):
        queryset=User.objects.all()
        user=get_object_or_404(queryset,pk=pk)
        serializer=UserSerializer(user)
        return Response(serializer.data)



