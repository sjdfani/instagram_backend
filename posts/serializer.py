from rest_framework import serializers
from .models import Post, Tags
from account.models import Account


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class CreatePostSerializer(serializers.Serializer):
    # file = serializers.FileField()
    title = serializers.CharField(max_length=50)
    caption = serializers.CharField(max_length=200)
    tags = serializers.SlugRelatedField(many=True, slug_field='name', queryset=Tags.objects.all()
                                        )

    def create(self, validated_data):
        # file = validated_data['file']
        title = validated_data['title']
        caption = validated_data['caption']
        tags = validated_data['tags']
        request = self.context['request']
        account = Account.objects.get(user=request.user)
        post = Post.objects.create(
            account=account, title=title, caption=caption
        )
        post.tags.set(tags)
        return post

    def to_representation(self, instance):
        res = super().to_representation(instance)
        res['tags'] = TagsSerializer(instance.tags.all(), many=True).data
        return res

    def to_internal_value(self, data):
        tags = data.get('tags', [])
        for tag in tags:
            Tags.objects.get_or_create(name=tag)
        return super().to_internal_value(data)
