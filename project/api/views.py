from rest_framework import viewsets, mixins
from .models import Post, Comment
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
    # Actually, I don't understand why we can set such permission classes
    # for ListCreate methods (ListCreate had only IsAuthenticatedOrReadOnly)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get_queryset(self):
        user_pk = self.kwargs.get('user_pk', None)
        if user_pk == None:
            return Post.objects.all()
        return Post.objects.filter(author_id = user_pk)

    def get_serializer_class(self):
        if self.action in ('list', 'create'):
            return api_serializers.PostListSerializer
        return api_serializers.PostDetailSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentReadOnlyViewSet(mixins.ListModelMixin,
    mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    # Creating, retrieving, listing comments of post
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        # If we don't look for Post's comments -> we look for User's comments
        if self.kwargs.get('post_pk', None) == None:
            return api_serializers.UserCommentSerializer
        return api_serializers.PostCommentSerializer

    def get_queryset(self):
        post_pk = self.kwargs.get('post_pk', None)
        # If we don't look for Post's comments -> we look for User's comments
        if post_pk == None:
            user_pk = self.kwargs.get('user_pk', None)
            return Comment.objects.filter(author_id = user_pk)
        return Comment.objects.filter(post_id = post_pk)


class CommentViewSet(CommentReadOnlyViewSet, mixins.CreateModelMixin, viewsets.GenericViewSet):

    def perform_create(self, serializer):
        serializer.save(
            author = self.request.user,
            post_id = self.kwargs.get('post_pk')
        )
