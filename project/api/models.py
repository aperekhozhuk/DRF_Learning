from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 300)
    text = models.TextField()
    author = models.ForeignKey(User, null=True, related_name='posts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, null=True, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=True, related_name='comments', on_delete=models.CASCADE)
