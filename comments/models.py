from django.db import models
from posts.models import Post
from account.models import Account


class Comments(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments_post')
    content = models.TextField()
    author = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='comments_acc', name='author')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Comment'

    def __str__(self) -> str:
        return self.post.account.user.email
