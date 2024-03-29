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
        res['post_count'] = Post.objects.filter(
            account__id=instance.id).count()
        res['follower_count'] = Follower.objects.filter(
            account__id=instance.id).count()
        res['follower_list'] = list(set(Follower.objects.filter(
            account__id=instance.id).values_list('follower__id', flat=True)))
        res['following_count'] = Following.objects.filter(
            account__id=instance.id).count()
        res['following_list'] = list(set(Following.objects.filter(
            account__id=instance.id).values_list('following__id', flat=True)))
        return res


class UpdateInformationSerializer(serializers.Serializer):
    bio = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=20)

    def update(self, instance, validated_data):
        instance.bio = validated_data.get('bio', instance.bio)
        instance.user.username = validated_data.get(
            'username', instance.user.username)
        instance.save()
        instance.user.save()
        return instance

    def save(self, **kwargs):
        request = self.context['request']
        account = Account.objects.get(user=request.user)
        self.update(account, self.validated_data)


class ChangeLanguageSerializer(serializers.Serializer):
    language = serializers.CharField(max_length=3)

    def validate_language(self, value):
        if value not in ['fa', 'en']:
            raise serializers.ValidationError(
                {'message': 'you can choose fa or en for language.'})
        return value

    def update(self, instance, validated_data):
        language = Language.PERSIAN if validated_data['language'] == "fa" else Language.ENGLISH
        instance.language = language
        instance.save()

    def save(self, **kwargs):
        account = Account.objects.get(user=self.context['request'].user)
        self.update(account, self.validated_data)


class ChangeProfilePhotoSerializer(serializers.Serializer):
    photo = serializers.ImageField()

    def update(self, instance, validated_data):
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()

    def save(self, **kwargs):
        account = Account.objects.get(user=self.context['request'].user)
        self.update(account, self.validated_data)


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
