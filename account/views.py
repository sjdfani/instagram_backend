from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Account
from .serializer import AccountSerializer, UpdateInformationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


class AccountDetails(ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request = self.request
        return Account.objects.filter(user=request.user)


class UpdateInformation(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = UpdateInformationSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)
