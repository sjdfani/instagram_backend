from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Account
from .serializer import AccountSerializer, UpdateInformationSerializer, ChangeLanguageSerializer, ChangeProfilePhotoSerializer, SetBirthdateSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser


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


class ChangeLanguage(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangeLanguageSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)


class ChangeProfilePhoto(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]

    def post(self, request):
        serializer = ChangeProfilePhotoSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)


class SetBirthdate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = SetBirthdateSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = {'message': 'Set birthdate is successful.'}
            return Response(message, status=status.HTTP_200_OK)
