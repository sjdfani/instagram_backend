from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializer import CreatePostSerializer, ListPostSerializer, RetrieveUpdateDestroyPostSerializer, RetrievePostSerializer, CommentStatusPostSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from follows.models import Following


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
        return Post.objects.filter(account__id=self.kwargs.get('pk'))


class RetrieveUpdateDestroyPost(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(Q(id=self.kwargs.get('pk')) & Q(account__user=user))

    def get_serializer_class(self):
        if self.request.method == "GET":
            return RetrievePostSerializer
        return RetrieveUpdateDestroyPostSerializer


class CommentStatusPost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CommentStatusPostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = {'message': 'change status is successful.'}
            return Response(message, status=status.HTTP_200_OK)


class ExplorerPosts(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListPostSerializer
    # pagination_class = BasePagination

    def get_queryset(self):
        return Post.objects.filter(~Q(account__user=self.request.user))


class HomePosts(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListPostSerializer

    def get_queryset(self):
        account_id = list(set(Following.objects.filter(account__user=self.request.user).values_list(
            'following__id', flat=True)))
        return Post.objects.filter(account__id__in=account_id)
