from dataclasses import fields

from rest_framework import serializers
from . models import Follower
class FollowerSerializer(serializers.ModelSerializer):
    owner=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model=Follower
        fields=['id','follower','owner']

