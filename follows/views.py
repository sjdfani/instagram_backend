from rest_framework.permissions import IsAuthenticated
from follows.models import Follower, Following
from .serializer import CreateFollowingSerializer, FollowerSerializer, FollowingSerializer, DestroyFollowingSerializer, DestroyFollowerSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateFollowing(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Following.objects.all()
    serializer_class = CreateFollowingSerializer


class DestroyFollowing(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, **kwargs):
        data = {
            'following': self.kwargs.get('pk')
        }
        serializer = DestroyFollowingSerializer(
            data=data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ListFollowing(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowingSerializer

    def get_queryset(self):
        return Following.objects.filter(account__id=self.kwargs.get('pk'))


class DestroyFollower(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, **kwargs):
        data = {
            'follower': self.kwargs.get('pk')
        }
        serializer = DestroyFollowerSerializer(
            data=data, context={'request': request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


class ListFollower(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(account__id=self.kwargs.get('pk'))
