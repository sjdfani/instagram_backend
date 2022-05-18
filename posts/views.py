from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializer import CreatePostSerializer, ListPostSerializer, RetrieveUpdateDestroyPostSerializer, RetrievePostSerializer


class CreatePost(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreatePostSerializer

    def get_queryset(self):
        request = self.request
        return Post.objects.filter(account__user=request.user)


class ListPost(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListPostSerializer

    def get_queryset(self):
        request = self.request
        return Post.objects.filter(account__user=request.user)


class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        request = self.request
        return Post.objects.filter(account__user=request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RetrievePostSerializer
        return RetrieveUpdateDestroyPostSerializer
