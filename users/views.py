from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.models import CustomUser
from .serializer import RegisterSerializer, LoginSerializer
from .utils import get_tokens_for_user


class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)


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
                return Response(tokens, status=status.HTTP_200_OK)
            else:
                message = {'password': 'your password is incorrect.'}
                return Response(message, status=status.HTTP_401_UNAUTHORIZED)
