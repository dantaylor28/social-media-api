from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Post
from pins.models import Pin
from tags.models import Tag
from likes.models import Like

class PostSerializer(serializers.ModelSerializer):
    """
    Numerous extra fields are present to show num_of_pins/
    comments, category name and more. Image validation is also
    present ensuring the file size, height and width doesn't
    exceed the maximum.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    post_image = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_image.url'
    )
    is_post_owner = serializers.SerializerMethodField()
    tags = serializers.ListField(
        child=serializers.CharField(max_length=30),
        write_only=True,
        required=False
    )
    tags_display = serializers.SerializerMethodField(read_only=True)
    pinned_id = serializers.SerializerMethodField()
    num_of_pins = serializers.ReadOnlyField()
    liked_id = serializers.SerializerMethodField()
    num_of_likes = serializers.ReadOnlyField()
    num_of_comments = serializers.ReadOnlyField()
    updated_at = serializers.SerializerMethodField()

    def validate_post_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError(
                "Image files cannot be larger than 2MB"
        )
        return value
    
    def get_post_image(self, obj):
        if obj.post_image:
            return obj.post_image.url
        return None

    def get_is_post_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner
    
    def get_pinned_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            pin = Pin.objects.filter(
                owner=user, post=obj
            ).first()
            return pin.id if pin else None
        
    def get_liked_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    def create(self, validated_data):
        request = self.context["request"]
        tags = validated_data.pop("tags", [])

        # Manually get uploaded image from request.FILES
        image = request.FILES.get("post_image")
        # Create post first
        post = Post.objects.create(**validated_data)

        # Explicitly assign image
        if image:
            post.post_image = image
            post.save()
        self._handle_tags(post, tags)
        return post

    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)
        post = super().update(instance, validated_data)

        if tags is not None:
            post.tags.clear()
            self._handle_tags(post, tags)
        
        return post
    
    def _handle_tags(self, post, tags):
        for tag_name in tags:
            tag_name = tag_name.strip().lower()
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

    def get_tags_display(self, obj):
        return [tag.name for tag in obj.tags.all()]

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'caption', 'owner', 'is_post_owner',
            'uploaded_at', 'updated_at', 'post_image', 'profile_id',
            'profile_image', 'pinned_id', 'num_of_pins', 'liked_id',
            'num_of_likes', 'num_of_comments', 'tags', 'tags_display',
        ]