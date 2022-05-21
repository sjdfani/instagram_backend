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

    def validate_language(self, value):
        if value not in ['fa', 'en']:
            raise serializers.ValidationError(
                'you can choose fa or en for language.')
        return value

    def save(self, **kwargs):
        language = self.validated_data['language']
        request = self.context['request']
        account = Account.objects.get(user=request.user)
        if language == 'fa':
            account.language = Language.PERSIAN
        elif language == 'en':
            account.language = Language.ENGLISH
        account.save()


class ChangeProfilePhotoSerializer(serializers.Serializer):
    photo = serializers.ImageField()

    def save(self, **kwargs):
        photo = self.validated_data['photo']
        request = self.context['request']
        account = Account.objects.get(user=request.user)
        account.photo = photo
        account.save()


class SetBirthdateSerializer(serializers.Serializer):
    birthdate = serializers.DateField()

    def save(self, **kwargs):
        request = self.context['request']
        birthdate = self.validated_data['birthdate']
        account = Account.objects.get(user=request.user)
        account.birthdate = birthdate
        account.save()
