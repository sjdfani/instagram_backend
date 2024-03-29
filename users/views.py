from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from account.serializer import AccountSerializer
from config.settings import Redis_object
from users.models import CustomUser
from .serializer import RegisterSerializer, LoginSerializer, ChangePasswordSerializer, ForgetPasswordSerializer, VerifyForgetPasswordSerializer, ChangeUsernameSerializer, ConfirmForgetPasswordSerializr
from .utils import get_tokens_for_user
from rest_framework.permissions import IsAuthenticated
from account.models import Account
from django.utils import timezone


class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            message = serializer.save()
            return Response(message, status=status.HTTP_201_CREATED)


class Login(APIView):
    def post(self, request):
        serializer = LoginSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                tokens = get_tokens_for_user(user)
                account = Account.objects.get(user=user)
                account.last_login = timezone.now()
                account.save()
                account_info = AccountSerializer(account)
                data = {
                    'account': account_info.data,
                    'tokens': tokens,
                    'message': 'Login is successful.'
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                message = {'message': 'Your password is incorrect.'}
                return Response(message, status=status.HTTP_401_UNAUTHORIZED)


class ChangePassword(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            user = CustomUser.objects.get(email=request.user.email)
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                message = {'message': 'Change password is successful.'}
                return Response(message, status=status.HTTP_200_OK)
            else:
                message = {'message': 'Your old password is incorrect.'}
                return Response(message, status=status.HTTP_401_UNAUTHORIZED)


class ForgetPassword(APIView):
    def post(self, request):
        serializer = ForgetPasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK)


class VerifyForgetPassword(APIView):
    def post(self, request):
        serializer = VerifyForgetPasswordSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            status, message = serializer.save()
            if status:
                return Response(message, status=status.HTTP_200_OK)
            else:
                return Response(message, status=status.HTTP_400_BAD_REQUEST)


class ConfirmForgetPassword(APIView):
    def post(self, request):
        serializer = ConfirmForgetPasswordSerializr(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            message = serializer.save()
            return Response(message, status=status.HTTP_200_OK)


class ChangeUsername(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = ChangeUsernameSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            message = serializer.save()
            return Response(message, status=status.HTTP_200_OK)
