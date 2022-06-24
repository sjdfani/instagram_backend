from rest_framework import serializers
from .models import Account, Language
from users.serializer import UserSerializer
from posts.models import Post
from follows.models import Follower, Following


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['user'] = UserSerializer(instance.user).data
        res['post'] = list(set(Post.objects.filter(
            account__id=instance.id).values_list('id', flat=True)))
        res['follower'] = list(set(Follower.objects.filter(
            account__id=instance.id).values_list('follower__id', flat=True)))
        res['following'] = list(set(Following.objects.filter(
            account__id=instance.id).values_list('following__id', flat=True)))
        return res


class UpdateInformationSerializer(serializers.Serializer):
    bio = serializers.CharField(max_length=200)

    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance


class ChangeLanguageSerializer(serializers.Serializer):
    language = serializers.CharField(max_length=3)

    def validate_language(self, value):
        if value not in ['fa', 'en']:
            raise serializers.ValidationError(
                {'message': 'you can choose fa or en for language.'})
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


class AccountInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'photo', 'bio', 'user']

    def username_info(self, obj):
        return {
            'username': obj.user.username
        }

    user = serializers.SerializerMethodField('username_info')


class ListAccountInformationSerializer(serializers.Serializer):
    accounts_id = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Account.objects.all()
    )

    def save(self, **kwargs):
        accounts_id = self.validated_data['accounts_id']
        return AccountInformationSerializer(accounts_id, many=True).data
