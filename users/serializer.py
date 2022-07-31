from rest_framework import serializers
from .models import CustomUser
from django.core.mail import send_mail
from config.settings import Redis_object, env
from .utils import number_generator
from account.models import Account


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=50)

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError({'message': 'Email is exists.'})
        return value

    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                {'message': 'username is exists.'})
        return value

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError(
                {'message': 'The size of password must be 6 or more.'})
        return value

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        password = validated_data['password']
        user = CustomUser.objects.create(
            email=email, username=username, password=password)
        user.set_password(password)
        user.save()
        Account.objects.create(user=user)

    def save(self, **kwargs):
        self.create(self.validated_data)
        return {'message': 'Register is successful.'}


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {'message': 'The email is not exists.'})
        return value


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password = serializers.CharField()


class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {'message': 'The email is not exists.'})
        return value

    def process(self, email):
        code = number_generator(5)
        print(f"code : {code}")
        Redis_object.set(email, code, 300)
        message = f'Your verify code is : {code}\nYour code will expire after 5 minute.\n\t\tGood luck'
        # send_mail('Forget password', message, env(
        #     'EMAIL_USEREMAIL'), [email], fail_silently=False)

    def save(self, **kwargs):
        email = self.validated_data['email']
        self.process(email)


class VerifyForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {'message': 'The email is not exists.'})
        return value

    def process(self, email, code):
        redis_code = Redis_object.get(email)
        if code == redis_code:
            return (True, {'message': 'Your input code is correct.'})
        else:
            return (False, {'message': 'Your input code is invalid.'})

    def save(self, **kwargs):
        email = self.validated_data['email']
        code = self.validated_data['code']
        return self.process(email, code)


class ConfirmForgetPasswordSerializr(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate_email(self, value):
        if not CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {'message': 'The email is not exists.'})
        return value

    def process(self, email, password):
        user = CustomUser.objects.get(email=email)
        user.set_password(password)
        user.save()
        return {'message': 'Change password is successful.'}

    def save(self, **kwargs):
        email = self.validated_data['email']
        password = self.validated_data['password']
        return self.process(email, password)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class ChangeUsernameSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.save()

    def save(self, **kwargs):
        user = CustomUser.objects.get(email=self.context['request'].user.email)
        self.update(user, self.validated_data)
        return {'message': 'Change username is successful.'}
