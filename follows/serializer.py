from rest_framework import serializers
from .models import Follower, Following
from account.models import Account
from account.serializer import AccountSerializer


class CreateFollowingSerializer(serializers.Serializer):
    following = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all()
    )
    account = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all()
    )

    def validate(self, attrs):
        following = attrs['following']
        account = attrs['account']
        if Following.objects.filter(following=following, account=account).exists():
            raise serializers.ValidationError(
                {'message': 'you followed this account.'})
        return attrs

    def create(self, validated_data):
        following = validated_data['following']
        account = validated_data['account']
        return Following.objects.create(account=account, following=following)


class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['account'] = AccountSerializer(
            instance.account, context={'request': request}
        ).data
        res['following'] = AccountSerializer(
            instance.following, context={'request': request}
        ).data
        return res


class CreateFollowerSerializer(serializers.Serializer):
    follower = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all()
    )
    account = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all()
    )

    def validate(self, attrs):
        follower = attrs['follower']
        account = attrs['account']
        if Follower.objects.filter(follower=follower, account=account).exists():
            raise serializers.ValidationError(
                {'message': 'you have this account as follower.'})
        return attrs

    def create(self, validated_data):
        follower = validated_data['follower']
        account = validated_data['account']
        return Follower.objects.create(account=account, follower=follower)


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['account'] = AccountSerializer(
            instance.account, context={'request': request}
        ).data
        res['follower'] = AccountSerializer(
            instance.follower, context={'request': request}
        ).data
        return res
