from rest_framework.generics import ListAPIView
from .models import Account
from .serializer import AccountSerializer
from rest_framework.permissions import IsAuthenticated


class AccountDetails(ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request = self.request
        return Account.objects.filter(user=request.user)
