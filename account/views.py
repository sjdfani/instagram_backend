from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.views import APIView
from .models import Account
from .serializer import AccountSerializer, UpdateInformationSerializer, ChangeLanguageSerializer, ChangeProfilePhotoSerializer, ListAccountInformationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from django.db.models import Q
import random
from follows.models import Following


class AccountDetails(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.filter(pk=self.kwargs.get('pk'))


class UpdateInformation(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UpdateInformationSerializer

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)


class ChangeLanguage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangeLanguageSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = {'message': 'Change language is successful.'}
            return Response(message, status=status.HTTP_200_OK)


class ChangeProfilePhoto(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = ChangeProfilePhotoSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = {'message': 'Change profile photo is successful.'}
            return Response(message, status=status.HTTP_200_OK)


class ListAccountInformation(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ListAccountInformationSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            data = serializer.save()
            return Response(data=data, status=status.HTTP_200_OK)


class SuggestionAccount(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer

    def get_queryset(self):
        accounts_id = list(set(Following.objects.filter(
            account__user=self.request.user).values_list('following__id', flat=True)))
        lookup = ~Q(user=self.request.user) & ~Q(id__in=accounts_id)
        obj = list(Account.objects.filter(lookup))
        obj_count = Account.objects.filter(lookup).count()
        count = obj_count if obj_count < 20 else 20
        return random.sample(obj, count)
