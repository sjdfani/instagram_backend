from rest_framework.permissions import IsAuthenticated
from follows.models import Follower, Following
from .serializer import CreateFollowerSerializer, CreateFollowingSerializer, FollowerSerializer, FollowingSerializer
from rest_framework.generics import CreateAPIView, RetrieveDestroyAPIView, ListAPIView


class CreateFollowing(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Following.objects.all()
    serializer_class = CreateFollowingSerializer


class RetrieveDestroyFollowing(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Following.objects.all()
    serializer_class = FollowingSerializer


class ListFollowing(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowingSerializer

    def get_queryset(self):
        return Following.objects.filter(account__user=self.request.user)


class AnotherListFollowing(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowingSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Following.objects.filter(account__id=pk)


class CreateFollower(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Follower.objects.all()
    serializer_class = CreateFollowerSerializer


class RetrieveDestroyFollower(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer


class ListFollower(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        return Follower.objects.filter(account__user=self.request.user)


class AnotherListFollower(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FollowerSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Follower.objects.filter(account__id=pk)
