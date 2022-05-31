from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView
from .serializer import CreateLikeSerializer, ListLikeSerializer
from .models import Like
from rest_framework.permissions import IsAuthenticated


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


class RetrieveDestroyLike(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListLikeSerializer
    queryset = Like.objects.all()
