from django.db import models
from users.models import CustomUser


class Language(models.TextChoices):
    PERSIAN = ('Fa', 'fa')
    ENGLISH = ('En', 'en')


class Account(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to='profile-photo/', null=True, blank=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    language = models.CharField(
        max_length=10, choices=Language.choices, default=Language.PERSIAN)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.email
