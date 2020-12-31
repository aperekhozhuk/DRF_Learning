from rest_framework import viewsets
from .models import Post
from django.contrib.auth.models import User
from . import serializers as api_serializers
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return api_serializers.UserListSerializer
        return api_serializers.UserDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    # Actually, I don't understand why we can set such permission classes
    # for ListCreate methods (ListCreate had only IsAuthenticatedOrReadOnly)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return api_serializers.PostListSerializer
        return api_serializers.PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
