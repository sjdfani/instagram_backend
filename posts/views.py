from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated,Http404
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
    def get_queryset(self):
        request = self.request
        return Post.objects.filter(account__user=request.user)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RetrievePostSerializer
        return RetrieveUpdateDestroyPostSerializer

    def get_permissions(self):
        permissions_list = []
        if self.request.method in ['GET', 'PATCH', 'DELETE']:
            permissions_list.append(IsAuthenticated)
        # else:
        #     permissions_list.append()
        return [permission() for permission in permissions_list]
