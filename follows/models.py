from django.db import models
from account.models import Account


class Following(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='following_acc')
    following = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='following_foll')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.account.user.email
