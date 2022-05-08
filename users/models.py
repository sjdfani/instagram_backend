from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
