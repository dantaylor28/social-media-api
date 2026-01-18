from rest_framework import serializers
from .models import Tag

class TagSerializer(serializers.ModelSerializer):
    posts_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = ["id", "name", "posts_count"]
