from rest_framework.permissions import IsAuthenticated
from follows.models import Following
from .serializer import CreateFollowingSerializer, FollowingSerializer
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
