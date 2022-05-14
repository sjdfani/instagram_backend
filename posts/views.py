from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializer import CreatePostSerializer


class CreatePost(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreatePostSerializer

    def get_queryset(self):
        request = self.request
        return Post.objects.filter(account__user=request.user)
