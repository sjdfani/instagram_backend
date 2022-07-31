from rest_framework import serializers
from account.models import Account
from .models import Like
from posts.models import Post
from account.serializer import AccountSerializer


class CreateLikeSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )

    def validate(self, attrs):
        post = attrs['post']
        account = Account.objects.get(user=self.context['request'].user)
        if Like.objects.filter(post=post, account=account).exists():
            raise serializers.ValidationError(
                {'message': 'you liked this post.'})
        return attrs

    def create(self, validated_data):
        post = validated_data['post']
        account = Account.objects.get(user=self.context['request'].user)
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


class DestroyLikeSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )

    def validate(self, attrs):
        account = Account.objects.get(user=self.context['request'].user)
        post = attrs['post']
        if not Like.objects.filter(account=account, post=post).exists():
            raise serializers.ValidationError(
                {'message': "you don't like this post."}
            )
        return attrs

    def save(self, **kwargs):
        account = Account.objects.get(user=self.context['request'].user)
        post = self.validated_data['post']
        obj = Like.objects.get(account=account, post=post)
        obj.delete()
