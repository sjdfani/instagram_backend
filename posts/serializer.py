from rest_framework import serializers
from .models import Post, Tags
from account.models import Account
from account.serializer import AccountSerializer
from likes.models import Like
from archives.models import Archive
from django.db.models import Q


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['name']


class CreatePostSerializer(serializers.Serializer):
    file = serializers.FileField()
    title = serializers.CharField(max_length=50)
    caption = serializers.CharField(max_length=2000, required=False)
    tags = serializers.SlugRelatedField(
        many=True, slug_field='name', queryset=Tags.objects.all())
    comment_status = serializers.BooleanField()

    def create(self, validated_data):
        file = validated_data['file']
        title = validated_data['title']
        caption = validated_data.get('caption')
        tags = validated_data['tags']
        comment_status = validated_data['comment_status']
        request = self.context['request']
        account = Account.objects.get(user=request.user)
        post = Post.objects.create(
            account=account, file=file, title=title, caption=caption, comment_status=comment_status
        )
        post.tags.set(tags)
        return post

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['tags'] = TagsSerializer(instance.tags.all(), many=True).data
        return res

    def to_internal_value(self, data: dict):
        copy_data = data.copy()
        tags = copy_data.pop('tags', [])
        for tag in tags:
            Tags.objects.get_or_create(name=tag)
        tags = data.get('tags', [])
        return super().to_internal_value(data)


class ListPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['tags'] = TagsSerializer(instance.tags, many=True).data
        res['account'] = AccountSerializer(
            instance.account, context={'request': request}).data
        archive_objects = Archive.objects.filter(
            post=instance.id).values_list('account__id', flat=True)
        res['account_archives'] = list(set(archive_objects))
        res['like_count'] = Like.objects.filter(post__id=instance.id).count()
        res['is_like'] = Like.objects.filter(
            Q(post_id=instance.id) & Q(account__user=request.user)).exists()
        return res


class RetrieveUpdateDestroyPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    caption = serializers.CharField(max_length=200)
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tags.objects.all()
                                        )
    comment_status = serializers.BooleanField()

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.caption = validated_data.get('caption', instance.caption)
        instance.comment_status = validated_data.get(
            'comment_status', instance.comment_status)
        tags_state = validated_data.get('tags', None)
        if tags_state:
            instance.tags.clear()
            instance.tags.set(validated_data.get('tags', instance.tags))
        instance.save()
        return instance

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['tags'] = TagsSerializer(instance.tags, many=True).data
        return res

    def to_internal_value(self, data):
        tags = data.get('tags', [])
        for tag in tags:
            Tags.objects.get_or_create(name=tag)
        return super().to_internal_value(data)


class RetrievePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context['request']
        res = super().to_representation(instance)
        res['tags'] = TagsSerializer(instance.tags, many=True).data
        res['account'] = AccountSerializer(
            instance.account, context={'request': request}).data
        archive_objects = Archive.objects.filter(
            post=instance.id).values_list('account__id', flat=True)
        res['account_archives'] = list(set(archive_objects))
        res['like_count'] = Like.objects.filter(post__id=instance.id).count()
        res['is_like'] = Like.objects.filter(
            Q(post_id=instance.id) & Q(account__user=request.user)).exists()
        return res


class CommentStatusPostSerializer(serializers.Serializer):
    post = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all()
    )
    status = serializers.BooleanField()

    def save(self, **kwargs):
        post = self.validated_data['post']
        post.comment_status = self.validated_data['status']
        post.save()
