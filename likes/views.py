from rest_framework.generics import CreateAPIView, ListAPIView
from .serializer import CreateLikeSerializer, ListLikeSerializer, DestroyLikeSerializer
from .models import Like
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateLike(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateLikeSerializer
    queryset = Like.objects.all()


class ListLike(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListLikeSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Like.objects.filter(post__pk=pk)


class DestroyLike(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, **kwargs):
        data = {
            'post': self.kwargs.get('pk')
        }
        serializer = DestroyLikeSerializer(
            data=data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
