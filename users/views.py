from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import RegisterSerializer


class Register(APIView):
    def post(self, request):
        serializer = RegisterSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
