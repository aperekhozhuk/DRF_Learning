from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'user_id')
        extra_kwargs = {'text': {'write_only': True}}


class PostDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'user_id')


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']
