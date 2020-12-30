from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='author.id')
    url = serializers.HyperlinkedIdentityField(view_name='post-detail', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'user_id', 'url')
        extra_kwargs = {'text': {'write_only': True}}


class PostDetailSerializer(serializers.ModelSerializer):
    user_id = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'user_id')


class UserListSerializer(serializers.ModelSerializer):
    profile = serializers.HyperlinkedIdentityField(view_name='user-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'profile']


class UserDetailSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']
