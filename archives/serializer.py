from rest_framework import serializers
from archives.models import Archive
from posts.models import Post
from account.models import Account
from posts.serializer import ListPostSerializer


class CreateArchivePostSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )

    def validate_post(self, value):
        if Archive.objects.filter(post=value).exists():
            raise serializers.ValidationError('You archived this post.')
        return value

    def create(self, validated_data):
        request = self.context['request']
        account = Account.objects.get(user=request.user)
        post = validated_data['post']
        return Archive.objects.create(account=account, post=post)


class ListArchiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Archive
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['post'] = ListPostSerializer(
            instance.post, context={'request': request}).data
        return res
