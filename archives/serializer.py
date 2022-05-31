from rest_framework import serializers
from archives.models import Archive
from posts.models import Post
from account.models import Account
from posts.serializer import ListPostSerializer


class CreateArchivePostSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )
    account = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all()
    )

    def validate(self, attrs):
        post = attrs['post']
        account = attrs['account']
        if Archive.objects.filter(post=post, account=account).exists():
            raise serializers.ValidationError(
                {'message': 'you archived this post.'})
        return attrs

    def create(self, validated_data):
        account = validated_data['account']
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
