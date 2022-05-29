from django.db import models
from posts.models import Post
from account.models import Account


class Archive(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='archive_acc')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='archive_post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.account.user.email
