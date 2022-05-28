from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Comments
from rest_framework.permissions import IsAuthenticated
from .serializer import CreateCommentsSerializer, ListCommentsSerializer


class CreateComments(CreateAPIView):
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCommentsSerializer


class ListComments(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListCommentsSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comments.objects.filter(post__pk=pk)
