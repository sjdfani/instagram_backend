from django.db import models
from account.models import Account


class Tags(models.Model):
    name = models.CharField(max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, name='account')
    file = models.FileField(upload_to='posts/')
    title = models.CharField(max_length=50)
    caption = models.TextField()
    tags = models.ManyToManyField(Tags, name='tags')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    comment_status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
