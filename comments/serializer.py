from rest_framework import serializers

from account.models import Account
from .models import Comments
from posts.models import Post


class CreateCommentsSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )
    content = serializers.CharField(max_length=500)

    def create(self, validated_data):
        request = self.context['request']
        post = validated_data['post']
        content = validated_data['content']
        account = Account.objects.get(user=request.user)
        return Comments.objects.create(post=post, author=account, content=content)
