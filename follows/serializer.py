from rest_framework import serializers
from .models import Following
from account.models import Account
from account.serializer import AccountSerializer


class CreateFollowingSerializer(serializers.Serializer):
    following = serializers.PrimaryKeyRelatedField(
        queryset=Account.objects.all())

    def validate_following(self, value):
        if Following.objects.filter(following=value).exists():
            raise serializers.ValidationError('you followed this account')
        return value

    def create(self, validated_data):
        request = self.context['request']
        following = validated_data['following']
        account = Account.objects.get(user=request.user)
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
