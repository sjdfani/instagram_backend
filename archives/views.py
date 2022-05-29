from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveDestroyAPIView
from .models import Archive
from rest_framework.permissions import IsAuthenticated
from .serializer import CreateArchivePostSerializer, ListArchiveSerializer


class CreateArchivePost(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateArchivePostSerializer
    queryset = Archive.objects.all()


class ListArchivePost(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListArchiveSerializer

    def get_queryset(self):
        return Archive.objects.filter(account__user=self.request.user)


class RetrieveDestroyArchivePost(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListArchiveSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Archive.objects.filter(pk=pk)
