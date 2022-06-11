from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Archive
from rest_framework.permissions import IsAuthenticated
from .serializer import CreateArchivePostSerializer, ListArchiveSerializer, DestroyArchiveSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateArchivePost(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateArchivePostSerializer
    queryset = Archive.objects.all()


class ListArchivePost(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListArchiveSerializer

    def get_queryset(self):
        return Archive.objects.filter(account__user=self.request.user)


class DestroyArchivePost(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, **kwargs):
        data = {
            'account': self.kwargs.get('pk_1'),
            'post': self.kwargs.get('pk_2')
        }
        serializer = DestroyArchiveSerializer(
            data=data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {'message': 'delete is successful.'}
            return Response(data=data, status=status.HTTP_204_NO_CONTENT)
