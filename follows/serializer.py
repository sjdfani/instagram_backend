from rest_framework import serializers
from .models import Follower, Following
from account.models import Account
from account.serializer import AccountSerializer


class CreateFollowingSerializer(serializers.Serializer):
    following = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all()
    )

    def validate(self, attrs):
        following = attrs['following']
        account = Account.objects.get(user=self.context['request'].user)
        if Following.objects.filter(following=following, account=account).exists():
            raise serializers.ValidationError(
                {'message': 'you followed this account.'})
        return attrs

    def create(self, validated_data):
        following = validated_data['following']
        account = Account.objects.get(user=self.context['request'].user)
        Follower.objects.create(account=following, follower=account)
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


class DestroyFollowingSerializer(serializers.Serializer):
    following = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all()
    )

    def validate(self, attrs):
        following = attrs['following']
        account = Account.objects.get(user=self.context['request'].user)
        if not Following.objects.filter(following=following, account=account).exists():
            raise serializers.ValidationError(
                {'message': 'you do not follow this account.'})
        return attrs

    def delete_obj(self, validated_data):
        account = Account.objects.get(user=self.context['request'].user)
        following = validated_data['following']
        obj = Following.objects.get(account=account, following=following)
        obj.delete()

    def save(self, **kwargs):
        self.delete_obj(self.validated_data)


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


class DestroyFollowerSerializer(serializers.Serializer):
    follower = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all()
    )

    def validate(self, attrs):
        follower = attrs['follower']
        account = Account.objects.get(user=self.context['request'].user)
        if not Follower.objects.filter(follower=follower, account=account).exists():
            raise serializers.ValidationError(
                {'message': 'you do not follow this account.'})
        return attrs

    def delete_obj(self, validated_data):
        account = Account.objects.get(user=self.context['request'].user)
        follower = validated_data['follower']
        obj = Follower.objects.get(account=account, follower=follower)
        obj.delete()

    def save(self, **kwargs):
        self.delete_obj(self.validated_data)
