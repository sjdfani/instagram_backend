from rest_framework import serializers

from account.models import Account
from .models import Like
from posts.models import Post
from account.serializer import AccountSerializer


class CreateLikeSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )
    account = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all()
    )

    def validate_account(self, value):
        if Like.objects.filter(account=value).exists():
            raise serializers.ValidationError('you liked this post.')
        return value

    def create(self, validated_data):
        post = validated_data['post']
        account = validated_data['account']
        return Like.objects.create(post=post, account=account)


class ListLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['account'] = AccountSerializer(
            instance.account, context={'request': request}).data
        return res
