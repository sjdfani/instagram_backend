from rest_framework import serializers
from .models import Account, Language
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


class ChangeLanguageSerializer(serializers.Serializer):
    language = serializers.CharField(max_length=3)

    def save(self, **kwargs):
        language = self.validated_data['language']
        request = self.context['request']
        account = Account.objects.get(user=request.user)
        if language == 'fa':
            account.language = Language.PERSIAN
        elif language == 'en':
            account.language = Language.ENGLISH
        account.save()
