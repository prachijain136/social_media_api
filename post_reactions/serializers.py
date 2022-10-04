from .models import Like,Dislike
from rest_framework import serializers

class LikeSerializer(serializers.ModelSerializer):
    owner_like=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Like
        fields = ['id','post_like','owner_like']

class DislikeSerializer(serializers.ModelSerializer):
    owner_dislike=serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Dislike
        fields = ['id','post_dislike','owner_dislike']