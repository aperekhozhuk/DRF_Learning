from rest_framework import generics
from .models import Post
from . import serializers as api_serializers
from django.contrib.auth.models import User
from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_overview(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'posts': reverse('post-list', request=request, format=format)
    })

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = api_serializers.PostListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = api_serializers.PostDetailSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = api_serializers.UserListSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = api_serializers.UserDetailSerializer
