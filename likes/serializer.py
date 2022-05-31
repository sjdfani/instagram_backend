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

    def validate(self, attrs):
        post = attrs['post']
        account = attrs['account']
        if Like.objects.filter(post=post, account=account).exists():
            raise serializers.ValidationError(
                {'message': 'you liked this post.'})
        return attrs

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
