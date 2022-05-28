from rest_framework.generics import CreateAPIView
from .models import Comments
from rest_framework.permissions import IsAuthenticated
from .serializer import CreateCommentsSerializer


class CreateComments(CreateAPIView):
    queryset = Comments.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CreateCommentsSerializer
