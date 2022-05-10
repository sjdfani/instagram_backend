from rest_framework import serializers
from .models import Account
from users.serializer import UserSerializer


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['user'] = UserSerializer(instance.user).data
        return res


class UpdateInformationSerializer(serializers.Serializer):
    bio = serializers.CharField(max_length=200)
    birthdate = serializers.DateField()

    def save(self, **kwargs):
        bio = self.validated_data['bio']
        birthdate = self.validated_data['birthdate']
        request = self.context['request']
        account = Account.objects.get(user=request.user)
        account.bio = bio
        account.birthdate = birthdate
        account.save()
